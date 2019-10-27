# coding=utf-8
from selenium import webdriver
import time
import datetime

today = datetime.datetime.today() 
link = "https://test-basket.genotek.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_css_selector(".showcase-item:nth-child(1) > .showcase-item-cell:nth-child(2) button")
    button.click()
    time.sleep(2)
    button1 = browser.find_element_by_class_name("cell-btn")
    button1.click()
    time.sleep(3)
    input1 = browser.find_element_by_css_selector("input.suggestions-input")
    input1.send_keys("Test_" + today.strftime("%Y_%m_%d_%H_%M_%S") + " Test_" + today.strftime("%Y_%m_%d_%H_%M_%S"))
    input2 = browser.find_element_by_name("phone")
    input2.send_keys("89278564930")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("malyshenko@genotek.ru")
    input4 = browser.find_element_by_class_name("react-dadata__input")
    input4.send_keys("чебоксары энгельса 4 32")
    time.sleep(3)
    button2 = browser.find_element_by_class_name("react-dadata__suggestion")
    button2.click()
    option1 = browser.find_element_by_class_name("custom-control-label")
    option1.click()
    time.sleep(1)
    button3 = browser.find_element_by_css_selector("[type='submit']")
    button3.click()    

finally:
    # �������� ����������� ��� �� 30 ������
    time.sleep(50)
    # ��������� ������� ����� ���� �����������
    browser.quit()

# �� �������� �������� ������ ������ � ����� �����

