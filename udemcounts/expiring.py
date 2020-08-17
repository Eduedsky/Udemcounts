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

        print()

        # for record in csv_file:
        csv_writer.writerow([expiring_title,learning_platform, expiring_link, expiring_img_link, expiring_course_price, expiring_course_price_sale, link])
    csv_file.close()