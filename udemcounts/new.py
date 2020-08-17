from bs4 import BeautifulSoup
import requests
import csv 
import time
import datetime


def newcourses():
    pg = 0
    coupon = 0

    while True:
        pg += 1
        new_url = "https://www.real.discount/new/page/"
        pag = str(pg)
        new_url += pag
        print(new_url)
        
        #create a resonse object then extract the source code
        new_data = requests.get(new_url).text
        #pass the data through beautifulsoup
        new_soup = BeautifulSoup(new_data, "html.parser")

        #open csv file
        csv_file = open('new_courses.csv', 'w')

        #create rows for the csv file
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Course Name', 'Learning Platform', 'Course Link', 'Image Link', 'Discounted Price', 'Initial Price', 'Coupon Link'])
        
        for new_courses in new_soup.find_all(class_="col-sm-4 masonry-item"):
            coupon += 1
            print("Coupon: " + str(coupon))

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

                # locate learning platform
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
                #course expiration date
                course_expiration_date = coupon_link.find('span', class_="deal-countdown")
                course_expiration_date = course_expiration_date['data-expire']
                current_date = datetime.datetime.now()
                expiry_date = datetime.datetime.fromtimestamp(1500000000)
                print("Coupon Expiration Date: " + course_expiration_date)

            except:
                link = None
                course_expiration_date = None
                learning_platform = None


            # for record in csv_file:
            print()

            csv_writer.writerow([new_title, learning_platform, new_link, new_img_link, new_course_price, new_course_price_sale, link])
            new_dict = {
                "title": new_title
            }
            if len(new_title) == 0:
                break
            else:
                new_dict.clear() 
    csv_file.close()
    
newcourses()