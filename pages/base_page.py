from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.__wait = Wait(driver, timeout, 0.3)

    # element
    def is_visible(self, locator: str) -> WebElement:
        """Waiting on element and return WebElement if it is visible"""
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def is_present(self, locator: str) -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM"""
        return self.__wait.until(EC.presence_of_element_located(locator))

    def is_not_present(self, locator: str) -> WebElement:
        """Wait on element until it disappears """
        return self.__wait.until(EC.invisibility_of_element_located(locator))

    # elements
    def are_visible(self, locator: str) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible"""
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def are_present(self, locator: str) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM"""
        return self.__wait.until(EC.presence_of_all_elements_located(locator))