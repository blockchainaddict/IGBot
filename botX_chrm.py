from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import datetime


def login(driver):
    driver.get("https://www.instagram.com/")
    sleep(2)

    username = driver.find_element_by_css_selector('[name="username"]')
    password = driver.find_element_by_css_selector('[name="password"]')
    login = driver.find_element_by_css_selector("button")

    username.send_keys('your Ig Account')
    sleep(2)
    password.send_keys('your Password')
    sleep(2)
    login.click()
    sleep(5)

def open_tag(driver, url):
    sleepy_time = randint(4, 7)
    driver.get(url)
    sleep(sleepy_time)

    pictures = driver.find_elements_by_css_selector('div[class="_9AhH0"]')[9:13]
    image_count = 0

    for picture in pictures:
        if image_count >= 4:
            break

        picture.click()
        sleep(sleepy_time)

        heart = driver.find_element_by_css_selector('svg[aria-label="Like"]')
        heart.click()
        print('> Image liked')
        sleep(3)

        close_pic = driver.find_element_by_css_selector('[aria-label="Close"]')
        close_pic.click()
        sleep(3)

        image_count += 1
        #print(image_count, "images liked")
        sleep(sleepy_time)

def main():
    driver = webdriver.Chrome('/Users/user/PycharmProjects/igbot1/chromedriver')
    login(driver)

    tags = [
        'f4f',
        'l4l',
        'lifestyle',
        'happy'
    ]

    for tag in tags:
        open_tag(driver, f"https://www.instagram.com/explore/tags/{tag}")
        print('Done with', tag)

main()

file_tracker = open('igbot_tracker.txt', '+a')
fhand = file_tracker

linecount = 0

fhand.write('\nRun')

fhand.seek(0)
for lines in fhand:
    linecount += 1

print(linecount)