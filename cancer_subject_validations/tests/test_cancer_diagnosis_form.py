from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from ..form_validators import CancerDiagnosisFormValidator


class TestCancerDiagnosisForm(TestCase):

    def test_diagnosis_yes_category_required(self):
        '''Asserts raises exception if diagnosis is yes and
        required cancer category is missing.'''

        cleaned_data = {
            'diagnosis': YES,
            'cancer_category': None,
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('cancer_category', form_validator._errors)

    def test_diagnosis_yes_date_diagnosed_required(self):
        '''Asserts raises exception if diagnosis is yes and
        required date diagnosed is missing.'''

        cleaned_data = {
            'diagnosis': YES,
            'date_diagnosed': None,
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('date_diagnosed', form_validator._errors)

    def test_diagnosis_yes_diagnosis_basis_required(self):
        '''Asserts raises exception if diagnosis is yes and
        required diagnosis basis is missing.'''

        cleaned_data = {
            'diagnosis': YES,
            'diagnosis_basis': None,
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('diagnosis_basis', form_validator._errors)

    def test_diagnosis_yes_category_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'diagnosis': YES,
            'cancer_category': 'relapsed',
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_diagnosis_yes_date_diagnosed_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'diagnosis': YES,
            'date_diagnosed': get_utcnow(),
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_diagnosis_yes_diagnosis_basis_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'diagnosis': YES,
            'diagnosis_basis': 'clinical_only',
        }
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_date_diagnosed_valid_cancer_site_required(self):
        '''Asserts raises exception if date diagnosed is provided and
        required cancer site is missing.'''

        cleaned_data = {
            'date_diagnosed': get_utcnow(),
            'cancer_site': None}
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cancer_site', form_validator._errors)

    def test_date_diagnosed_valid_cancer_site_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'date_diagnosed': get_utcnow(),
            'cancer_site': 'C123.4'}
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_date_diagnosed_valid_diagnosis_word_required(self):
        '''Asserts raises exception if date diagnosed is provided and
        required diagnosis description is missing.'''

        cleaned_data = {
            'date_diagnosed': get_utcnow(),
            'diagnosis_word': None}
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('diagnosis_word', form_validator._errors)

    def test_date_diagnosed_valid_diagnosis_word_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'date_diagnosed': get_utcnow(),
            'diagnosis_word': 'cancer diagnosis desc.'}
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_diagnosis_no_invalid(self):
        '''Asserts raises exception if diagnosis is no,
        answer to diagnosis must be yes.'''

        cleaned_data = {
            'diagnosis': NO}
        form_validator = CancerDiagnosisFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('diagnosis', form_validator._errors)
