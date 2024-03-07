from selenium.webdriver.common.by import By
from Pages.BasePage import Base
from Configs.Locators import Locators

class Home(Base):
   
   
    def _init_(self, driver):
        self.driver = driver

    def scroll_down(self):
        homepage_text = self.wait_for(Locators.homepage_elem_loc).text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        subsciption_button_text = self.wait_for(Locators.subscription_elem_loc).text
        print(subsciption_button_text)
        return homepage_text, subsciption_button_text
        
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        homepage_text1 = self.wait_for(Locators.homepage_elem_loc).text
        return homepage_text1