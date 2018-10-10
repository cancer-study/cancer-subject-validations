from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..form_validators import BaseLineHivHistoryFormValidator


@tag('c')
class TestBaseLineHivHistoryForm(TestCase):

    def test_cd4_results_yes_invalid(self):
        cleaned_data = {
             "has_cd4": YES,
             "cd4_result": None,
         }
        form_validator = BaseLineHivHistoryFormValidator(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cd4_result', form_validator._errors)
