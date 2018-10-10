from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validators import BaseRiskAssessementCancerFormValidator


class TestBaseRiskAssessmentCancerForm(TestCase):

    def test_family_cancer_type_yes_invalid(self):
        '''Assert raises if any relative has had any cancer but
        none is declared
        '''
        cleaned_data = {
             "family_cancer": YES,
             "family_cancer_type": None,
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('family_cancer_type', form_validator._errors)

    def test_family_cancer_type_no_invalid(self):
        '''Assert raises if any relative has had any cancer
        is no and type is declared
        '''
        cleaned_data = {
             "family_cancer": NO,
             "family_cancer_type": 'blahblah',
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('family_cancer_type', form_validator._errors)

    def test_family_cancer_type_valid(self):
        '''Assert raises if any relative has had any cancer,
        is yes and type defined
        '''
        cleaned_data = {
             "family_cancer": YES,
             "family_cancer_type": 'blahblah',
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_family_cancer_type_no_valid(self):
        '''Assert raises if any relative has had any cancer,
        is no and none
        '''
        cleaned_data = {
             "family_cancer": NO,
             "family_cancer_type": None,
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_yes_invalid(self):
        '''Assert raise if subject has had a previous cancer,
        is yes and none
        '''
        cleaned_data = {
            "had_previous_cancer": YES,
            "previous_cancer": None,
            }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_no_invalid(self):
        '''Assert raise if subject has had a previous cancer,
        is non and none
        '''
        cleaned_data = {
             "had_previous_cancer": NO,
             "previous_cancer": None,
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_no_valid(self):
        '''Assert raise if subject has had a previous cancer,
        is no and type defined
        '''
        cleaned_data = {
             "had_previous_cancer": NO,
             "previous_cancer": 'None',
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_yes_valid(self):
        '''Assert raise if subject has had a previous cancer,
        is yes and none
        '''
        cleaned_data = {
             "had_previous_cancer": YES,
             "previous_cancer": 'None',
         }
        form_validator = BaseRiskAssessementCancerFormValidator(
             cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
