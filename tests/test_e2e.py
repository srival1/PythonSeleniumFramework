# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
import time


class Test_End2End(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        log.info("*******End to End Test Began**************")
        homePage = HomePage(self.driver)
        log.info("*******Clicking Shop Button***************")
        productPage = homePage.shopItems()
        products_list = productPage.getProducts()
        log.info("*******Extracted List of Products*********")
        # Below code is for list of products
        prod_list = ['Blackberry', 'iphone X', 'Samsung Note 8']

        for product in products_list:
            if productPage.getProductName(product).text in prod_list:
                productPage.clickAddToCart(product).click()
        log.info("*******Added Required Products to Cart***")
        checkoutPage = productPage.CheckoutButton()

        confirmPage = checkoutPage.CheckoutButton2()
        confirmPage.countryName().send_keys("indi")
        confirmPage.indiaLocation().click()
        confirmPage.setTermsCheckbox()
        #time.sleep(3)
        confirmPage.purchaseButton().click()
        log.info("*******Clicked on Purchase Button*********")
        message = confirmPage.alertMsg().text
        assert "Success! Thank you!" in message
        assert message.__contains__("Success! Thank you!")
        log.info("*******End to End Test Successfully Ended*")