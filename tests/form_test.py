import time

import pytest

from generator.generator import generated_person, generated_testing_data
from pages.form_page import FormPage


@pytest.mark.usefixtures('setup')
class TestFormPage:

    #form checks
    @pytest.mark.parametrize("name, surname, email, password", [('', '', '', ''),
                                                                ('', '', '', '')])
    def test_vaidation_form(self, name, surname, email, password):
        form_page = FormPage(self.driver)
        form_page.validation_check(name, surname, email, password)

    @pytest.mark.parametrize("name, surname, email, password", [('', '', '', ''),
                                                                ('', '', '', '')])
    def test_invalid_form(self, name, surname, email, password):
        form_page = FormPage(self.driver)
        form_page.validation_check(name, surname, email, password)

    # positive checks
    @pytest.mark.parametrize("name", generated_testing_data('../generator/test_src/valid_name.csv').list_data)
    def test_vaidation_name(self, name):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.validation_check(name, person.surname, person.email, person.password)

    @pytest.mark.parametrize("surname", generated_testing_data('../generator/test_src/valid_surname.csv').list_data)
    def test_vaidation_surname(self, surname):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.validation_check(person.name, surname, person.email, person.password)

    @pytest.mark.parametrize("email", [])
    def test_vaidation_email(self, email):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.validation_check(person.name, person.surname, email, person.password)

    @pytest.mark.parametrize("password", [])
    def test_vaidation_password(self, password):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.validation_check(person.name, person.surname, person.email, password)

    @pytest.mark.parametrize("name", generated_testing_data('../generator/test_src/invalid_name.csv').list_data)
    def test_invalid_name(self, name):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.invalid_check(name, person.surname, person.email, person.password)

    @pytest.mark.parametrize("surname", [])
    def test_invalid_surname(self, surname):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.invalid_check(person.name, surname, person.email, person.password)

    @pytest.mark.parametrize("email", [])
    def test_invalid_email(self, email):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.invalid_check(person.name, person.surname, email, person.password)

    @pytest.mark.parametrize("password", [])
    def test_invalid_password(self, password):
        form_page = FormPage(self.driver)
        person = generated_person()
        form_page.invalid_check(person.name, person.surname, person.email, password)