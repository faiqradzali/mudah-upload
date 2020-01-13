#!/usr/local/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import random
import string
import datetime
import time
import os

for file in range(1, 21, 1):
# Create a new instance of the Firefox driver

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome("/root/mudah/chromedriver", chrome_options=options)

    
    # go to the google home page
    driver.get("https://proniaga.mudah.my")
    adlink = ("https://www2.mudah.my/ai/form/1?draft=1&ca=9_s")
    inputElement = driver.find_element_by_name("email")
    inputElement.send_keys("EMAIL")
    inputElement = driver.find_element_by_name("passwd")
    inputElement.send_keys("PASSWORD")
    inputElement.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)

    # driver.find_element_by_xpath('//*[@id="abuse-announcement-modal"]/div/div/div[3]/button').click()
    f = open("script/SKMAGIC/" + str(file) + ".txt", "r")
    with open('csv/mudah_log.csv','a') as log:
        
        folder = f.read(3)
        f.readline()
        subject = f.readline()
        subject = subject[:-1]
        caption = f.readline()
        price = f.readline()
        caption = caption.replace(r'\n', '\n')
        time_start = datetime.datetime.now()

        print (time_start, "Filename:", file)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/div[1]/div[4]/div[1]/div/a').click()
        #driver.get(adlink)
        state = 1
        while state < 17:
            driver.implicitly_wait(30)
            for i in range(0, 6, 1):
                xpath = '//*[@id="image_' + str(i) + '"]'    
                uploadImg = driver.find_element_by_xpath(xpath)
                imgpath = 'C:/Users/faiqradzali/Desktop/ECOMMERCE/MUDAH/photos/SKMAGIC/' + folder + '/' + str(i+1) +'.jpg'
                uploadImg.send_keys(imgpath);
                
            randsubject = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            randcaption = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

            subject_temp = subject + " " + randsubject
            caption_temp = caption + randcaption
            driver.find_element_by_id("condition_New").click()
                
            driver.find_element_by_xpath('//*[@id="subject"]').send_keys(subject_temp)
            driver.find_element_by_xpath('//*[@id="body"]').send_keys(caption_temp)
            driver.find_element_by_xpath('//*[@id="price"]').send_keys(price)
            
            print (subject_temp)
            if state == 13:
                state +=3
                    
            select = Select(driver.find_element_by_xpath('//*[@id="region"]'))
            select.select_by_value(str(state))
            select = Select(driver.find_element_by_xpath('//*[@id="area"]'))
            if state == 1:#perlis
                area = random.randint(1, 7)
                select.select_by_index(area)
            elif state == 2:#kedah
                area = random.randint(1, 31)
                select.select_by_index(area)
            elif state == 3:#penang
                area = random.randint(1, 60)
                select.select_by_index(area)
            elif state == 4:#kelantan
                area = random.randint(1, 23)
                select.select_by_index(area)
                
            elif state == 5:#terengganu
                area = random.randint(1, 8)
                select.select_by_index(area)
              
            elif state == 6:#perak
                area = random.randint(1, 73)
                select.select_by_index(area)
           
            elif state == 7:#pahang
                area = random.randint(1, 37)
                select.select_by_index(area)
             
            elif state == 8:#selangor
                area = random.randint(1, 81)
                select.select_by_index(area)
              
            elif state == 9:#kl
                area = random.randint(1, 60)
                select.select_by_index(area)
               
            elif state == 10:#n9
                area = random.randint(1, 32)
                select.select_by_index(area)
                
            elif state == 11:#melaka
                area = random.randint(1, 19)
                select.select_by_index(area)
               
            elif state == 12:#johor
                area = random.randint(1, 51)
                select.select_by_index(area)
               
            elif state == 16:#pj
                area = 1
                select.select_by_index(area)
         
                
            driver.find_element_by_xpath('//*[@id="c_publish"]').click()
            driver.implicitly_wait(30)
            #driver.get("https://www2.mudah.my/ai/form/0?draft=1&ca=9_s")
            driver.find_element_by_xpath('//*[@id="ty-upsell-container"]/div[2]/div/div/div[2]/div/a').click()
            
            state+=1
            log.write("%s,%s,%s,%s,%s,%s,%s\n" % (time_start, datetime.datetime.now(), file, subject_temp, price, state, area))
        driver.quit()
        f.close()

   
    
    
        