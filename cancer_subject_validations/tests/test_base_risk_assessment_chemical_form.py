from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import BaseRiskAssessmentChemicalValidation
from django.core.exceptions import ValidationError
from edc_base.utils import get_utcnow


class TestBaseRiskAssessmentChemicalForm(TestCase):

    def test_abestos_yes(self):
        '''Assert raises if subject has worked with asbestos,
        how long has he/she worked with it
        '''
        cleaned_data = {
            "abestos": YES,
            "abestos_no_protection": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abestos_no_protection', form_validator._errors)

    def test_abestos_no(self):
        '''Assert raises if subject has worked with asbestos,
        how long has he/she worked with it
        '''
        cleaned_data = {
            "abestos": NO,
            "abestos_no_protection": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abestos_no_protection', form_validator._errors)

    def test_abestos_no_error(self):
        '''Assert raises if subject has worked with asbestos,
        how long has he/she worked with it
        '''
        cleaned_data = {
            "abestos": NO,
            "abestos_no_protection": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abestos_valid(self):
        '''Assert raises if subject has worked with asbestos,
        how long has he/she worked with it
        '''
        cleaned_data = {
            "abestos": YES,
            "abestos_no_protection": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_chemicals_yes(self):
        '''Assert raises if subject has worked with any of the chemicals,
        how long has it been
        '''
        cleaned_data = {
            "chemicals": YES,
            "chemicals_time": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemicals_time', form_validator._errors)

    def test_other_chemicals_no(self):
        '''Assert raises if subject has worked with any of the chemicals,
        how long has it been
        '''
        cleaned_data = {
            "chemicals": NO,
            "chemicals_time": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemicals_time', form_validator._errors)

    def test_other_chemicals_no_error(self):
        '''Assert raises if subject has worked with any of the chemicals,
        how long has it been
        '''
        cleaned_data = {
            "chemicals": NO,
            "chemicals_time": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_chemicals_valid(self):
        '''Assert raises if subject has worked with any of the chemicals,
        how long has it been
        '''
        cleaned_data = {
            "chemicals": YES,
            "chemicals_time": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arsenic_smelting_yes(self):
        '''Assert raises if subject has ever been
        involved in arsenic smelting,how long has it been
        '''
        cleaned_data = {
            "arsenic_smelting": YES,
            "total_time_no_protection": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('total_time_no_protection', form_validator._errors)

    def test_arsenic_smelting_no(self):
        '''Assert raises if subject has ever been
        involved in arsenic smelting,how long has it been
        '''
        cleaned_data = {
            "arsenic_smelting": NO,
            "total_time_no_protection": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('total_time_no_protection', form_validator._errors)

    def test_arsenic_smelting_no_error(self):
        '''Assert raises if subject has ever been
        involved in arsenic smelting,how long has it been
        '''
        cleaned_data = {
            "arsenic_smelting": NO,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arsenic_smelting_valid(self):
        '''Assert raises if subject has ever been
        involved in arsenic smelting,how long has it been
        '''
        cleaned_data = {
            "arsenic_smelting": YES,
            "total_time_no_protection": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
