import time

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def field_color(self):
        pass

    def fill_fields_and_submit(self, name, surname, email, password):
        self.is_visible(Locators.NAME).send_keys(name)
        self.is_visible(Locators.SURNAME).send_keys(surname)
        self.is_visible(Locators.EMAIL).send_keys(email)
        self.is_visible(Locators.PASSWORD).send_keys(password)
        self.is_visible(Locators.SUBMIT).click()
        time.sleep(3)