import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as GeckoOptions


browser = 'chrome'

@pytest.fixture
def driver_2(request, browser=browser):
    if browser == 'chrome':
        option = Options()
    elif browser == 'edge':
        option = EdgeOptions()
    elif browser == 'firefox':
        option = GeckoOptions

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-dev-shm-usage") 
    option.add_argument("--no-sandbox")
    option.add_argument("--mute-audio")
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    
    
    if browser == 'chrome':
        driver_2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    elif browser == 'edge':
        driver_2 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == 'IE':
        driver_2 = webdriver.Ie(service=IEService(IEDriverManager(log_level=20).install()))
    elif browser == 'firefox':
        driver_2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    request.cls.driver_2 = driver_2
    
    driver_2.get("https://automationexercise.com/")
    driver_2.maximize_window()
    

 