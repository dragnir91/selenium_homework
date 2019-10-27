# coding=utf-8
from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test_selenium.txt')           # добавляем к этому пути имя файла 
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input2 = browser.find_element_by_name("firstname")
    input2.send_keys("Andrey")
    input3 = browser.find_element_by_name("lastname")
    input3.send_keys("Malyshenko")
    input4 = browser.find_element_by_name("email")
    input4.send_keys("a.s.malyshenko@gmail.com")
    input5 = browser.find_element_by_id("file")
    input5.send_keys(file_path)

    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()  

finally:
    time.sleep(15)
    browser.quit()


