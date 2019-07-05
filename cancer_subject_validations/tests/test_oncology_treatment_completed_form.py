from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import (YES, NO)
from ..form_validators import (
                OncologyTreatmentCompletedFormValidator)


class TestOncologyTreatmentCompletedForm(TestCase):

    def test_had_chemo_treatment_details_required(self):
        '''Asserts raises exception on required treatment details missing
        if patient had chemotherapy.'''

        cleaned_data = {
            'patient_had_chemo': YES,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_had_chemo_treatment_details_provided(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly.'''

        cleaned_data = {
            'patient_had_chemo': YES,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')

    def test_had_radiation_treatment_details_required(self):
        '''Asserts raises exception on required treatment details missing
        if patient had radiation.'''

        cleaned_data = {
            'patient_had_radiation': YES,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_had_radiation_treatment_details_provided(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly.'''

        cleaned_data = {
            'patient_had_radiation': YES,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')

    def test_had_surgery_treatment_details_required(self):
        '''Asserts raises exception on required treatment details missing
        if patient had surgery.'''

        cleaned_data = {
            'patient_had_surgery': YES,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_had_surgery_treatment_details_provided(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly.'''

        cleaned_data = {
            'patient_had_surgery': YES,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')

    def test_no_chemo_treatment_details_invalid(self):
        '''Asserts raises exception for treatment details provided
        if patient did not have chemotherapy.'''

        cleaned_data = {
            'patient_had_chemo': NO,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_no_chemo_treatment_details_valid(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly'''

        cleaned_data = {
            'patient_had_chemo': NO,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')

    def test_no_radiation_treatment_details_invalid(self):
        '''Asserts raises exception for treatment details provided
        if patient did not have radiation treatment.'''

        cleaned_data = {
            'patient_had_radiation': NO,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_no_radiation_treatment_details_valid(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly'''

        cleaned_data = {
            'patient_had_radiation': NO,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')

    def test_no_surgery_treatment_details_invalid(self):
        '''Asserts raises exception for treatment details provided
        if patient did not have surgery.'''

        cleaned_data = {
            'patient_had_surgery': NO,
            'treatment_detail': 'given on some date'}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('treatment_detail', form_validator._errors)

    def test_no_surgery_treatment_details_valid(self):
        '''Tests cleaned data validates or fails tests if exception is
        raised unexpectedly'''

        cleaned_data = {
            'patient_had_surgery': NO,
            'treatment_detail': None}
        form_validator = OncologyTreatmentCompletedFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raise unexpectedly. Got{e}')
