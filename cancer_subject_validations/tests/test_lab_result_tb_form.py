from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import NO
from ..form_validators import LabResultTbFormValidator


class TestLabResultTbForm(TestCase):

    def test_tb_treatment_ipt_yes_start_required(self):
        cleaned_data = {
            'tb_treatment': 'Yes_(IPT)',
            'tb_treatment_start': None
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_treatment_start', form_validator._errors)

    def test_tb_treatment_ipt_yes_start_valid(self):
        cleaned_data = {
            'tb_treatment': 'Yes_(IPT)',
            'tb_treatment_start': get_utcnow()
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
    
    def test_tb_treatment_att_yes_start_required(self):
        cleaned_data = {
            'tb_treatment': 'Yes_(ATT)',
            'tb_treatment_start': None
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_treatment_start', form_validator._errors)
    
    def test_tb_treatment_att_yes_start_valid(self):
        cleaned_data = {
            'tb_treatment': 'Yes_(ATT)',
            'tb_treatment_start': get_utcnow()
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
    
    def test_tb_treatment_no_valid(self):
        cleaned_data = {
            'tb_treatment': NO,
            'tb_treatment_start': None
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
    
    def test_tb_treatment_no_invalid(self):
        cleaned_data = {
            'tb_treatment': NO,
            'tb_treatment_start': get_utcnow()
        }
        form_validator = LabResultTbFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_treatment_start', form_validator._errors)
