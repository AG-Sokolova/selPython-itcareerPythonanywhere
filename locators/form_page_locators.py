from selenium.webdriver.common.by import By

class FormPageLocators:

    NAME = (By.CSS_SELECTOR, '#name')
    SURNAME = (By.CSS_SELECTOR, '#surname')
    EMAIL = (By.CSS_SELECTOR, '#email')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    SUBMIT = (By.XPATH, '/html/body/div[2]/div/div/form/center/button')

    RESULT = (By.XPATH, '/html/body/div[2]/div/div/div/strong')
    RESULT_DESCRIPTION = (By.XPATH, '/html/body/div[2]/div/div/div')