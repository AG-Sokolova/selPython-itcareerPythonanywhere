from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):
    def fill_fields_and_submit(self, name='', surname='', email='', password=''):
        self.is_visible(Locators.NAME).send_keys(name)
        self.is_visible(Locators.SURNAME).send_keys(surname)
        self.is_visible(Locators.EMAIL).send_keys(email)
        self.is_visible(Locators.PASSWORD).send_keys(password)
        self.is_visible(Locators.SUBMIT).click()
        result = self.is_present(Locators.RESULT).text
        result_description = self.is_present(Locators.RESULT_DESCRIPTION).text.replace(result, '')
        return result, result_description

    def validation_check(self, name='', surname='', email='', password=''):
        SUCCESS = "Success!"
        SUCCESS_DESCRIPTION: str = f'Hello: {name} {surname}'
        output = self. fill_fields_and_submit(name, surname, email, password)
        result: str = output[0].strip()
        result_description: str = output[1].strip()
        assert result == SUCCESS, f'INVILED RESULT:{result} == {SUCCESS}'
        assert result_description == SUCCESS_DESCRIPTION,  f'INVILED RESULT: {result_description} == {SUCCESS_DESCRIPTION}'

    def invalid_check(self, name='', surname='', email='', password=''):
        ERROR = "Error:"
        ERROR_DESCRIPTION = "All Fields are Required"
        output = self.fill_fields_and_submit(name, surname, email, password)
        result: str = output[0].strip()
        result_description: str = output[1].strip()
        assert result == ERROR,  f'INVILED RESULT:{result} == {ERROR}'
        assert result_description == ERROR_DESCRIPTION,  f'INVILED RESULT: {result_description} == {ERROR_DESCRIPTION}'


