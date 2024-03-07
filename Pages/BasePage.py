from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:

  def __init__(self, driver):
           self.driver=driver
           self._wait = WebDriverWait(self.driver, 10)

  def wait_for(self, locator):
    return self._wait.until(ec.presence_of_element_located(locator))

  def wait_for_click(self, locator):
    return self._wait.until(ec.element_to_be_clickable(locator))
  
  def wait_for_visible(self, locator):
    return self._wait.until(ec.visibility_of_element_located(locator))

  def find(self, locator):
      return self.driver.find_elements(*locator)