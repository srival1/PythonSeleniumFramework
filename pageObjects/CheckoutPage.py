from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkoutButton2 = (By.CSS_SELECTOR, ".btn-success")

    def CheckoutButton2(self):
        self.driver.find_element(*CheckoutPage.checkoutButton2).click()
        confirmPage = ConfirmationPage(self.driver)
        return confirmPage
