from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from edc_form_validators import form_validator

from ..form_validators import BaseLineHivHistoryFormValidator


@tag('c')
class TestBaseLineHivHistoryForm(TestCase):

    def test_cd4_results_yes_invalid(self):
        """Assert that has_cd4 requires cd4 results 
        """
        cleaned_data = {
             "has_cd4": YES,
             "cd4_result": None,
         }
        form_validator = BaseLineHivHistoryFormValidator(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_result', form_validator._errors)
        
    def test_cd4_results_no_invalid(self):
        cleaned_data = {
            "has_cd4":NO,
            "cd4_result":10,
            }
        form_validator = BaseLineHivHistoryFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_result', form_validator._errors)   
        
    def test_cd4_results_no_valid(self):        
        cleaned_data = {
             "has_cd4": NO,
             "cd4_result": None,
         }
        form_validator = BaseLineHivHistoryFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')   
