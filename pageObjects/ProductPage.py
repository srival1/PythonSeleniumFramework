from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, ".card")
    productName = (By.CSS_SELECTOR, "h4 a")
    addToCart = (By.CSS_SELECTOR, "button")
    checkoutButton = (By.PARTIAL_LINK_TEXT, "Checkout")

    def getProducts(self):
        return self.driver.find_elements(*ProductPage.products)

    def getProductName(self, product):
        return product.find_element(*ProductPage.productName)

    def clickAddToCart(self, product):
        return product.find_element(*ProductPage.addToCart)

    def CheckoutButton(self):
        self.driver.find_element(*ProductPage.checkoutButton).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage


