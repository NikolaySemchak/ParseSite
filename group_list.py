from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import random
import os


def delay ():
    time.sleep(random.randint(3,5))

def Main ():
    USERNAME = "NEBOT"

    driver = webdriver.Chrome(os.getcwd() + "//chromedriver")

    #Вход в аккаунт
    driver.get("https://discord.com/")
    # browser.fullscreen_window()
    driver.find_element_by_xpath("//div/div/div[1]/div[2]/div/div[2]/button").click()
    driver.find_element_by_xpath("//div/div/div[1]/div[2]/div/div[2]/form/input").send_keys(USERNAME)
    driver.find_element_by_xpath("//div/div/div[1]/div[2]/div/div[2]/form/button").click()
    time.sleep(60)

    # driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    spam = ["Здарова писюнцы, я вернулся", "Оххх, как же я соскучился", "Оочень рад вас видеть"]

    for i in range(3):
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div').send_keys(spam[i])
        delay()





    # #Нажимаем на всплывающие окна

    # browser.find_element_by_xpath("//section/main/div/div/div/div/button").click()
    # time.sleep(1.5)
    # browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    # time.sleep(2)

    # #Ищем всех людей на которых подписаны

    # browser.get("https://www.instagram.com/nebotovskiy/")
    # time.sleep(1.5)
    # browser.find_element_by_xpath("//section/main/div/header/section/ul/li[3]/a").click()
    # time.sleep(1.5)
    # people = browser.find_elements_by_xpath('li')
    # print(people)



Main()