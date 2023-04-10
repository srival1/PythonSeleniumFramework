import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.homePageData import HomePageData
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):
    @pytest.mark.regression
    def test_signup(self, getSignupData):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        log.info("*******Home Page Test Began for " + getSignupData["name"] + "**************")
        homePage.getNameObject().send_keys(getSignupData["name"])
        homePage.getEmailObject().send_keys(getSignupData["email"])
        homePage.getPswdObject().send_keys(getSignupData["password"])
        homePage.getLoveIceObject().click()

        GenderDropdown = Select(homePage.getGenderObject())
        GenderDropdown.select_by_visible_text(getSignupData["gender"])

        if getSignupData["status"] == "student":
            homePage.getStudentObject().click()
        elif getSignupData["status"] == "employed":
            homePage.getEmployedObject().click()

        homePage.setDOB(getSignupData["dob"].date().strftime("%m/%d/%Y"))
        homePage.getTwoWayObject().clear()
        homePage.getSubmitObject().click()

        message = homePage.getAlertObject().text
        print(message)
        assert message.__contains__("Success")
        assert "Success" in message
        self.driver.refresh()
        log.info("*******Home Page Test End for "+getSignupData["name"]+"**************")
        log.handlers.clear()

    @pytest.fixture(params=HomePageData.getTestData("testcase1"))
    #@pytest.fixture(params=[{"name":"test1 name", "email":"test1@gmail.com", "password":"test1pswd", "gender":"Female", "dob":"12/31/2000"}, {"name":"test2 name", "email":"test2@gmail.com", "password":"test2pswd", "gender":"Male", "dob":"06/14/1999"}])
    def getSignupData(self, request):
        return request.param
