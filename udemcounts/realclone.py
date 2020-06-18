from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv 
import time
import datetime

#getting the webpage
url = "https://www.real.discount/"
new_url = "https://www.real.discount/new/"
expiring_soon_url = "https://www.real.discount/expiring-soon-coupons/"
few_remaining_url = "https://www.real.discount/few-remaining-coupons/"
most_enrolled_url = "https://www.real.discount/most-enrolled/"
page_url = "https://www.real.discount/new/page/"
category_url = "https://www.real.discount/search-page/offer_cat/"


def newcourses():
    #create a resonse object then extract the source code
    new_data = requests.get(new_url).text
    #pass the data through beautifulsoup
    new_soup = BeautifulSoup(new_data, "html.parser")

    #open csv file
    csv_file = open('new_courses.csv', 'w', encoding='utf-8')

    #create rows for the csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Course Name', 'Learning Platform', 'Course Link', 'Image Link', 'Discounted Price', 'Initial Price', 'Coupon Link'])
    
    for new_courses in new_soup.find_all(class_="col-sm-4 masonry-item"):
        # new_courses = new_soup.find(class_="col-sm-4 masonry-item")
        # expiring_courses = expiring_soup.find_all(class_="col-sm-3")
        # few_courses = few_soup.find_all(class_="col-sm-3")
        # most_courses = most_soup.find_all(class_="col-sm-3")
        # print(new_courses.prettify())

        # for new_courses in new_courses
        # locate title
        try:
            new_title = new_courses.h4.a.text.rstrip(" .")
            print("Course Name: " + new_title)
        except:
            new_title = None

        #locate course link
        try:
            new_link = new_courses.div.a['href']
            print("Real Discount Course Link: " + new_link)

        except:
            new_link = None


        #locate image link
        try: 
            new_img_link = new_courses.div.a.img['src']
            print("Course Image Link: " + new_img_link)
        except:
            new_img_link = None

        #locate course price
        try:
            new_course_price = new_courses.div.h5.text.split(' ', 1)[0]
            print("Discounted Course Prise: " + new_course_price)
        except:
            new_course_price = None
        #locate course price sale
        try:
            new_course_price_sale = new_courses.div.h5.text.split(' ', 1)[1]
            print("Initial Course Price: " + new_course_price_sale)
        except:
            new_course_price_sale = None

        # #locate coupon link
        try:
            new_coupon_link = requests.get(new_link).text
            new_coupon_link_soup = BeautifulSoup(new_coupon_link, "html.parser")
            coupon_link = new_coupon_link_soup.find(class_="roundedtopright roundedtopleft")
            link = coupon_link.find(class_='btn')['href']
            print("Course Link: " + link)

            #course expiration date
            course_expiration_date = coupon_link.find('span', class_="deal-countdown")
            course_expiration_date = course_expiration_date['data-expire']
            current_date = datetime.datetime.now()
            expiry_date = datetime.datetime.fromtimestamp(1500000000)
            print(course_expiration_date)

        except:
            link = None
            course_expiration_date = None
        #locate learning platform
        for learning_platform in link.split('/')[2]:
            try:
                if learning_platform == "click.linksynergy.com":
                    learning_platform = link.split('/')[6]
                    print("Learning Platform: " + learning_platform)
                else:
                    print("Learning Platform: " + learning_platform)
            except:
                learning_platform = None   
        #get coupon code
        if learning_platform == "www.eduonix.com":
            coupon_code = link.split('/')[3]
            coupon_code = link.split('=')[1]
            coupon_code = coupon_code.rstrip("&utm_source")
            print("Coupon code: " + coupon_code)
        elif learning_platform == "www.udemy.com":
            coupon_code = link.split('/')[5]
            coupon_code = link.split('?')[1]
            coupon_code = link.split('=')[1]
            print("Coupon code: " + coupon_code)
        else:
            if link.split('/')[2] == "click.linksynergy.com":
                coupon_code = link.split('/')[9]
                print("Coupon code: " + coupon_code)
            else:
                pass
        print("None")
        print()
        # for record in csv_file:
        csv_writer.writerow([new_title,learning_platform, new_link, new_img_link, new_course_price, new_course_price_sale, link])
    csv_file.close()
    expiringcourses()

def expiringcourses():
    #create a resonse object then extract the source code
    expiring_data = requests.get(expiring_soon_url).text
    #pass the data through beautifulsoup
    expiring_soup = BeautifulSoup(expiring_data, "html.parser")
    #open csv file
    csv_file = open('expiring_courses.csv', 'w', encoding='utf-8')

    #create rows for the csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Course Name', 'Learning Platform', 'Course Link', 'Image Link', 'Discounted Price', 'Initial Price', 'Coupon Link'])

    for expiring_courses in expiring_soup(class_="col-sm-3 masonry-item"):
        try:
            expiring_title = expiring_courses.h4.a.text.rstrip(" .")
            print("Course Name: " + expiring_title)
        except:
            expiring_title = None

        #locate course link
        try:
            expiring_link = expiring_courses.div.a['href']
            print("Real Discount Course Link: " + expiring_link)

        except:
            expiring_link = None


        #locate image link
        try: 
            expiring_img_link = expiring_courses.div.a.img['src']
            print("Course Image Link: " + expiring_img_link)
        except:
            expiring_img_link = None

        #locate course price
        try:
            expiring_course_price = expiring_courses.div.h5.text.split(' ', 1)[0]
            print("Discounted Course Prise: " + expiring_course_price)
        except:
            expiring_course_price = None
        #locate course price sale
        try:
            expiring_course_price_sale = expiring_courses.div.h5.text.split(' ', 1)[1]
            print("Initial Course Price: " + expiring_course_price_sale)
        except:
            expiring_course_price_sale = None

        # #locate coupon link
        try:
            expiring_coupon_link = requests.get(expiring_link).text
            expiring_coupon_link_soup = BeautifulSoup(expiring_coupon_link, "html.parser")
            coupon_link = expiring_coupon_link_soup.find(class_="roundedtopright roundedtopleft")
            link = coupon_link.find(class_='btn')['href']
            print("Course Link: " + link)

            #course expiration date
            course_expiration_date = coupon_link.find('span', class_="deal-countdown")
            course_expiration_date = course_expiration_date['data-expire']
            current_date = datetime.datetime.now()
            expiry_date = datetime.datetime.fromtimestamp(1500000000)
            print(course_expiration_date)

        except:
            link = None
            course_expiration_date = None
        #locate learning platform
        learning_platform = link.split('/')[2]
        if learning_platform == "click.linksynergy.com":
            learning_platform = link.split('/')[6]
            print("Learning Platform: " + learning_platform)
        else:
            print("Learning Platform: " + learning_platform)

        #get coupon code
        if learning_platform == "www.eduonix.com":
            coupon_code = link.split('/')[3]
            coupon_code = link.split('=')[1]
            coupon_code = coupon_code.rstrip("&utm_source")
            print("Coupon code: " + coupon_code)
        elif learning_platform == "www.udemy.com": 
            if link.split('/')[2] == "click.linksynergy.com":
                coupon_code = link.split('http')[1]
                coupon_code = link.split('/')[5]
                coupon_code = link.split('?')[1]
                coupon_code = link.split('=')[1]
                print("Coupon code: " + coupon_code)
            else:
                coupon_code = link.split('/')[5]
                coupon_code = link.split('?')[1]
                coupon_code = link.split('=')[1]
                print("Coupon code: " + coupon_code)

        else:
            print("Coupon code: ------")
        print()

        # for record in csv_file:
        csv_writer.writerow([expiring_title,learning_platform, expiring_link, expiring_img_link, expiring_course_price, expiring_course_price_sale, link])
    csv_file.close()
    fewremainingcourses()

def fewremainingcourses():
    #create a resonse object then extract the source code
    few_data = requests.get(few_remaining_url).text
    #pass the data through beautifulsoup
    few_soup = BeautifulSoup(few_data, "html.parser")
    #open csv file
    csv_file = open('few_remaining_courses.csv', 'w', encoding='utf-8')

    #create rows for the csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Course Name', 'Learning Platform', 'Course Link', 'Image Link', 'Discounted Price', 'Initial Price', 'Coupon Link'])

    for few_courses in few_soup(class_="col-sm-3 masonry-item"):
        try:
            few_title = few_courses.h4.a.text.rstrip(" .")
            print("Course Name: " + few_title)
        except:
            few_title = None

        #locate course link
        try:
            few_link = few_courses.div.a['href']
            print("Real Discount Course Link: " + few_link)

        except:
            few_link = None


        #locate image link
        try: 
            few_img_link = few_courses.div.a.img['src']
            print("Course Image Link: " + few_img_link)
        except:
            few_img_link = None

        #locate course price
        try:
            few_course_price = few_courses.div.h5.text.split(' ', 1)[0]
            print("Discounted Course Prise: " + few_course_price)
        except:
            few_course_price = None
        #locate course price sale
        try:
            few_course_price_sale = few_courses.div.h5.text.split(' ', 1)[1]
            print("Initial Course Price: " + few_course_price_sale)
        except:
            few_course_price_sale = None

        # #locate coupon link
        try:
            few_coupon_link = requests.get(few_link).text
            few_coupon_link_soup = BeautifulSoup(few_coupon_link, "html.parser")
            coupon_link = few_coupon_link_soup.find(class_="roundedtopright roundedtopleft")
            link = coupon_link.find(class_='btn')['href']
            print("Course Link: " + link)

            #course expiration date
            course_expiration_date = coupon_link.find('span', class_="deal-countdown")
            course_expiration_date = course_expiration_date['data-expire']
            current_date = datetime.datetime.now()
            expiry_date = datetime.datetime.fromtimestamp(1500000000)
            print(course_expiration_date)
            
        except:
            link = None
            course_expiration_date = None

        #locate learning platform
        learning_platform = link.split('/')[2]
        if learning_platform == "click.linksynergy.com":
            learning_platform = link.split('/')[6]
            print("Learning Platform: " + learning_platform)
        else:
            print("Learning Platform: " + learning_platform)

        #get coupon code
        if learning_platform == "www.eduonix.com":
            coupon_code = link.split('/')[3]
            coupon_code = link.split('=')[1]
            coupon_code = coupon_code.rstrip("&utm_source")
            print("Coupon code: " + coupon_code)
        elif learning_platform == "www.udemy.com": 
            if link.split('/')[2] == "click.linksynergy.com":
                coupon_code = link.split('http')[1]
                coupon_code = link.split('/')[5]
                coupon_code = link.split('?')[1]
                coupon_code = link.split('=')[1]
                print("Coupon code: " + coupon_code)
            else:
                coupon_code = link.split('/')[5]
                coupon_code = link.split('?')[1]
                coupon_code = link.split('=')[1]
                print("Coupon code: " + coupon_code)

        else:
            print("Coupon code: ------")

        print()

        # for record in csv_file:
        csv_writer.writerow([few_title,learning_platform, few_link, few_img_link, few_course_price, few_course_price_sale, link])
    csv_file.close()
    # mostenrolledcourses()

def search_courses():
    searchcourse = input("Enter name of the course to search")
    


newcourses()

# white-block-content
#editors choice

#promoted courses

#expired coupons

# print(coupon_link.prettify())

# #course duration
# new_course_duration = coupon_link.find(class_='fa fa-clock-o icon-margin')
# # print(new_course_duration)

# #locate course category
# course_category = coupon_link.find(class_="list-unstyled list-inline top-meta")
# # print(course_category)

# #locate remaining coupons
# remaining_coupons = coupon_link.div
# print(remaining_coupons)