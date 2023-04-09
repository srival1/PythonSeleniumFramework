from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.ProductPage import ProductPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
    name_textbox = (By.CSS_SELECTOR, "input[name='name']")
    email_textbox = (By.NAME, "email")
    password_textbox = (By.ID, "exampleInputPassword1")
    loveice_checkbox = (By.CLASS_NAME, "form-check-input")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    studentstatus_radio = (By.ID, "inlineRadio1")
    employedstatus_radio = (By.ID, "inlineRadio2")
    dob_spltextbox = (By.NAME, "bday")
    twoway_textbox = (By.CSS_SELECTOR, "input.ng-pristine")
    submit_button = (By.XPATH, "//input[@value='Submit']")
    alertmsg = (By.CSS_SELECTOR, "div.alert-success")

    def shopItems(self):

        #return self.driver.find_element(*HomePage.shop) # * will deserialize this TUPLE like below selenium step
        #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        self.driver.find_element(*HomePage.shop_link).click()
        productPage = ProductPage(self.driver)
        return productPage

    def getNameObject(self):
        return self.driver.find_element(*HomePage.name_textbox)

    def getEmailObject(self):
        return self.driver.find_element(*HomePage.email_textbox)

    def getPswdObject(self):
        return self.driver.find_element(*HomePage.password_textbox)

    def getLoveIceObject(self):
        return self.driver.find_element(*HomePage.loveice_checkbox)

    def getGenderObject(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    def getStudentObject(self):
        return self.driver.find_element(*HomePage.studentstatus_radio)

    def getEmployedObject(self):
        return self.driver.find_element(*HomePage.employedstatus_radio)

    def setDOB(self, date):
        dob_element = self.driver.find_element(*HomePage.dob_spltextbox)
        dob_element.click()
        dob_element.send_keys(date[0:2])
        dob_element.send_keys(date[3:5])
        dob_element.send_keys(date[6:])
        dob_element.send_keys(Keys.TAB)

    def getTwoWayObject(self):
        return self.driver.find_element(*HomePage.twoway_textbox)

    def getSubmitObject(self):
        return self.driver.find_element(*HomePage.submit_button)

    def getAlertObject(self):
        return self.driver.find_element(*HomePage.alertmsg)
