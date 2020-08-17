from bs4 import BeautifulSoup
import requests
import csv 
import time
import datetime

#getting the webpage
url = "https://www.real.discount/"
expiring_soon_url = "https://www.real.discount/expiring-soon-coupons/"
few_remaining_url = "https://www.real.discount/few-remaining-coupons/"
most_enrolled_url = "https://www.real.discount/most-enrolled/"
page_url = "https://www.real.discount/new/page/"
category_url = "https://www.real.discount/search-page/offer_cat/"




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