import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    # def selectOptionByText(self, locator, text):
    #     sel = Select(locator)
    #     sel.select_by_visible_text(text)

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('C:\\Users\\srika\\PycharmProjects\\PythonSeleniumFramework\\testLogs\\logfile.log')

        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object needs to be passed from above statement to connect the dots

        logger.setLevel(logging.DEBUG)
        return logger
