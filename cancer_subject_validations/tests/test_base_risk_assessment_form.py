from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import BaseRiskAssessmentFormValidator
from django.core.exceptions import ValidationError
from edc_base.utils import get_utcnow


class TestBaseRiskAssessmentForm(TestCase):

    def test_has_tubercolosis_valid(self):
        cleaned_data = {
            "tuberculosis": YES,
            "year_tb": None,
        }
        form_validator = BaseRiskAssessmentFormValidator(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('year_tb', form_validator._errors)

    def test_has_tubercolosis_not_valid(self):
        cleaned_data = {
            "tuberculosis": NO,
            "year_tb": get_utcnow(),
        }
        form_validator = BaseRiskAssessmentFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('year_tb', form_validator._errors)

    def test_has_tubercolosis_not_valid_no(self):
        cleaned_data = {
            "tuberculosis": NO,
            "year_tb": None,
        }
        form_validator = BaseRiskAssessmentFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_has_tuberclosis_valid_valid(self):
        cleaned_data = {
            "tuberculosis": YES,
            "year_tb": get_utcnow(),
        }
        form_validator = BaseRiskAssessmentFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
