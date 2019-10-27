# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    input1 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    input2 = browser.find_element_by_id("input_value")
    x = calc(input2.text)
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(x)

    button2 = browser.find_element_by_css_selector("[type='submit']")
    button2.click()  

finally:
    time.sleep(15)
    browser.quit()
