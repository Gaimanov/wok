from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


class ProductPageLocators:
    ADDED = (By.XPATH, '//strong[contains(text(), "Coders at Work")]')
    ADD_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    BASKET_MSG = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_MSG = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BASKET_EMPTY_MSG = (By.XPATH, '//p[contains(text(), "Your basket is empty")]')
    BASKET_EMPTY_PROOF = (By.XPATH, '//h2[contains(text(), "Totals")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            # WebDriverWait(self.browser, 2).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        except TimeoutException as e:
            print('ERROR ', e)

    def add_item_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket.click()

