# coding=utf-8
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]  
    browser.switch_to.window(new_window)

    input2 = browser.find_element_by_id("input_value")
    x = calc(input2.text)
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(x)

    button2 = browser.find_element_by_css_selector("[type='submit']")
    button2.click()  

finally:
    time.sleep(15)
    browser.quit()

