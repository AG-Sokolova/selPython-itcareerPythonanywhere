import time

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self, name, surname, email, password):
        self.is_visible(Locators.NAME).send_keys(name)
        time.sleep(3)
        self.is_visible(Locators.SURNAME).send_keys(surname)
        time.sleep(3)
        self.is_visible(Locators.EMAIL).send_keys(email)
        time.sleep(3)
        self.is_visible(Locators.PASSWORD).send_keys(password)
        time.sleep(3)
        self.is_visible(Locators.SUBMIT).click()
        time.sleep(3)