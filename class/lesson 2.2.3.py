from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



def calc(k,f):
    sum = int(k) + int(f)
    return sum


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    k_element = browser.find_element_by_id("num1").text
    f_element = browser.find_element_by_id("num2").text
    x = str(calc(k_element, f_element))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(13)
    browser.quit()

