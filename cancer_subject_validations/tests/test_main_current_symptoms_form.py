from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES


from ..form_validators import MainCurrentSymptomsFormValidation


class TestMainCurrentSymptomsFormValidation(TestCase):

    @tag('1')
    def test_symptom_details_yes1(self):
        """ symptom_desc is required if any_worry
        is YES
         """
        cleaned_data = {'any_worry': YES,
                        'symptom_desc': 'Explanation'}
        form_validator = MainCurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes2(self):
        """ patient_own_remedy is required if any_worry
        is YES
         """
        cleaned_data = {'any_worry': YES,
                        'patient_own_remedy': 'Explanation'}
        form_validator = MainCurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes3(self):
        """ severity is required if any_worry
        is YES
         """
        cleaned_data = {'any_worry': YES,
                        'severity': 'Explanation'}
        form_validator = MainCurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
