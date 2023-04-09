import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome" or browser_name == "Chrome" or browser_name == "CHROME":
        service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option('detach', True)
        # chrome_options.add_argument("headless") # headless mode for chrome
        # chrome_options.add_argument("--ignore-certificate-errors")
        # chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox" or browser_name == "Firefox" or browser_name == "FIREFOX":
        service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge" or browser_name == "Edge" or browser_name == "EDGE":
        service_obj = Service("C:\\Users\\srika\\Downloads\\Drivers\\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver

    yield
    driver.close()

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
        #driver.get_screenshot_as_file("C:\\Users\srika\\PycharmProjects\\PythonSeleniumFramework\\ScreenShots\\" + name)

    # @pytest.fixture(scope='session', autouse=True)
    # def configure_html_report_env(request):
    #     request.config._metadata.update(
    #         {'foo': 'bar'}
    #     )


