import pytest
from pages.form_page import FormPage


@pytest.mark.usefixtures('setup')
class TestFormPage:

    def test_form(self):
        form_page = FormPage(self.driver)
        name = 'Cheryl'
        surname = 'Hillman'
        email = 'c8kWwQFFjkNw9OUnKHyy6x_oIy2z@hotmail.com'
        password = 'jSA@1HDg'

        form_page.fill_fields_and_submit(name, surname, email, password)