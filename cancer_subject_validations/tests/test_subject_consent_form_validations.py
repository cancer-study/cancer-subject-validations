from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO, FEMALE, MALE

from ..form_validators import SubjectConsentFormValidation


@tag('csc')
class TestSubjectConsentForm(TestCase):

    def test_gender_identity_male_valid(self):
        cleaned_data = {
            'gender': MALE,
            'identity': '782311109',
        }
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_gender_identity_male_invalid(self):
        cleaned_data = {
            'gender': MALE,
            'identity': '782321109',
        }
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('identity', form_validator._errors)

    def test_gender_identity_female_valid(self):
        cleaned_data = {
            'gender': FEMALE,
            'identity': '782321109',
        }
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_gender_identity_female_invalid(self):
        cleaned_data = {
            'gender': FEMALE,
            'identity': '782311109',
        }
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('identity', form_validator._errors)
