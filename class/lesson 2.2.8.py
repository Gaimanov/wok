from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_name = "../5555.txt"
file_path = os.path.join(current_dir, file_name)
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys('Ilya')
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys('Ivanov')
    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input3.send_keys('shitshow@gmail.com')
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()