from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage():

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    purchase = (By.CSS_SELECTOR, ".btn-lg")
    alert = (By.CLASS_NAME, "alert")

    def countryName(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def indiaLocation(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ConfirmationPage.india))
        return self.driver.find_element(*ConfirmationPage.india)

    def setTermsCheckbox(self):
        self.driver.execute_script("document.getElementById('checkbox2').click()")

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

    def alertMsg(self):
        return self.driver.find_element(*ConfirmationPage.alert)
