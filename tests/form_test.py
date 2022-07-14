import pytest

from generator.generator import generated_person
from pages.form_page import FormPage


@pytest.mark.usefixtures('setup')
class TestFormPage:

    def test_form(self):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.fill_fields_and_submit(person.name, person.surname, person.email, person.password)