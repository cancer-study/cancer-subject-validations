from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import OTRRadiationFormValidation


class TestOTRRadiationForm(TestCase):

    def test_otrr_valid(self):
        '''Assert raises if patient radiation
        details are available, but missing concomitant
        '''
        cleaned_data = {
             'radiation_details': YES,
             'concomitant': None,
             'amount_radiation': True,
         }
        form_validator = OTRRadiationFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('concomitant', form_validator._errors)

    def test_otrr_invalid_yes(self):
        '''Assert raises if patient radiation
        details are available but amount_radiation is
        false
        '''
        cleaned_data = {
            'radiation_details': YES,
            'concomitant': YES,
            'amount_radiation': False,
            }
        form_validator = OTRRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amount_radiation', form_validator._errors)

    def test_orr_invalid_yes_concomitant(self):
        '''Assert raises if patient radiation details
        are available but concomitant is none
        '''
        cleaned_data = {
            'radiation_details': YES,
            'concomitant': None,
            'amount_radiation': True,
            }
        form_validator = OTRRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('concomitant', form_validator._errors)

    def test_otrr_valid_yes(self):
        '''True if patient radiation
        details are available and other required fields are valid.
        '''
        cleaned_data = {
             'radiation_details': YES,
             'concomitant': YES,
             'amount_radiation': True,
         }
        form_validator = OTRRadiationFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_otrr_invalid_yes_concomitant_none(self):
        '''Assert raises if patient radiation details
        are available but concomitant is yes
        and amount radiation is none.
        '''
        cleaned_data = {
            'radiation_details': YES,
            'concomitant': YES,
            'amount_radiation': None,
            }
        form_validator = OTRRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amount_radiation', form_validator._errors)

    def test_otrr_invalid_no(self):
        '''Assert raises if no patient radiation
        details are available but concomitant is yes.
        '''
        cleaned_data = {
             'radiation_details': NO,
             'concomitant': YES,
             'amount_radiation': False,

         }
        form_validator = OTRRadiationFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('concomitant', form_validator._errors)

    def test_otrr_valid_none(self):
        '''True if no radiation details.
        '''
        cleaned_data = {
             'radiation_details': NO,
             'concomitant': None,
             'amount_radiation': False,
         }
        form_validator = OTRRadiationFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_otrr_invalid_amount_radiation(self):
        '''Assert raises if no patient radiation
        details are available but amount_radiation is true.
        '''
        cleaned_data = {
            'radiation_details': NO,
            'concomitant': None,
            'amount_radiation': True,
            }
        form_validator = OTRRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('amount_radiation', form_validator._errors)
