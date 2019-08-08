from selenium import webdriver
import time
driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo1\\Driver\\chromedriver.exe")
driver.get("www.thetestingworld.com/testings/")
driver.maximize_window()
time.sleep(1)