from bs4 import BeautifulSoup
import requests
import csv 
import time
import datetime
import sys

    
class NewScraper:
    def __init__(self):
        #open csv file
        self.csv_file = open('few_remaining_courses.csv', 'w')
        #create rows for the csv file
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Course Name', 'Learning Platform', 'Course Link', 'Image Link', 'Discounted Price', 'Initial Price', 'Coupon Link'])
        self.scraper()

    def scraper(self):
        pg = 0
        coupon = 0

        while True:
            print()
            pg += 1
            page = str(pg)
            url = "https://www.real.discount/few-remaining-coupons/page/"
            url += page

            print(url)        

            #create a resonse object then extract the source code
            few_data = requests.get(url).text
            #pass the data through beautifulsoup
            few_soup = BeautifulSoup(few_data, "html.parser")

            for few_courses in few_soup(class_="col-sm-3 masonry-item"):
                print()
                coupon += 1
                print("Coupon:" + str(coupon))
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
                    pass
                self.csv_writer.writerow([few_title,learning_platform, few_link, few_img_link, few_course_price, few_course_price_sale, link])
                few_dict = {
                    "title": few_title
                }
                ctr = sum(map(len, few_dict.values()))
                print(ctr)
                if ctr == 0:
                    sys.exit()
                else:
                    few_dict.clear()  
                # for record in csv_file:
        self.csv_file.close()

if __name__ == '__main__':
    print("Scraping for Remaining Coupons")
    scrape = NewScraper()