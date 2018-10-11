from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validators import OTRChemoFormValidation


class TestBaseRiskAssessmentCancerForm(TestCase):

    def test_cancer_delayed_invalid(self):
        '''Assert raises if doses have been delayed is
        yes but no reason given
        '''
        cleaned_data = {
             "chemo_delayed": YES,
             "why_delayed": None,
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('why_delayed', form_validator._errors)

    def test_cancer_delayed_valid(self):
        '''True if chemo doses have been delayed is
        yes and reason is given.
        '''
        cleaned_data = {
             "chemo_delayed": YES,
             "why_delayed": 'Hematox',
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cancer_delayed_no_valid(self):
        '''True if chemo doses have been delayed is
        no and reason is not given.
        '''
        cleaned_data = {
             "chemo_delayed": NO,
             "why_delayed": None,
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cancer_delayed_no_invalid(self):
        '''Assert raises if chemo doses have been delayed is
        no but reason is given.
        '''
        cleaned_data = {
             "chemo_delayed": NO,
             "why_delayed": 'Hematox',
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('why_delayed', form_validator._errors)

    def test_cancer_reduced_invalid(self):
        '''Assert raises if chemo doses reduced is
        yes but no reason given.
        '''
        cleaned_data = {
             "chemo_reduced": YES,
             "why_reduced": None,
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('why_reduced', form_validator._errors)

    def test_cancer_reduced_valid(self):
        '''True if chemo doses reduced is
        yes and reason is given.
        '''
        cleaned_data = {
             "chemo_reduced": YES,
             "why_reduced": 'Hematox',
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cancer_reduced_no_invalid(self):
        '''Assert raises if chemo doses have been delayed is
        no but reason is given.
        '''
        cleaned_data = {
             "chemo_reduced": NO,
             "why_reduced": 'Hematox',
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('why_reduced', form_validator._errors)

    def test_cancer_reduced_no_valid(self):
        '''Assert true if doses have been delayed is
        no and reason none.
        '''
        cleaned_data = {
             "chemo_reduced": NO,
             "why_reduced": None,
         }
        form_validator = OTRChemoFormValidation(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
