# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    z = str(int(x_element.text) + int(y_element.text))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
