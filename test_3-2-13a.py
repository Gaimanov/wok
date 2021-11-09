from selenium import webdriver
import pytest
import unittest
import time


class TestClassName(unittest.TestCase):
    def test_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("Shitshow@gmail.com")
        input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
        input4.send_keys("88005252525")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
        input5.send_keys("Myxosransk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        actual = welcome_text_elt.text
        expected = 'Congratulations! You have successfully registered!'
        browser.quit()
        self.assertEqual(actual, expected, 'Wrong')

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input3.send_keys("Shitshow@gmail.com")
        input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
        input4.send_keys("88005252525")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
        input5.send_keys("Myxosransk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        actual = welcome_text_elt.text
        expected = 'Congratulations! You have successfully registered!'
        browser.quit()
        self.assertEqual(actual, expected, 'Wrong')


if __name__ == "__main__":
    unittest.main()