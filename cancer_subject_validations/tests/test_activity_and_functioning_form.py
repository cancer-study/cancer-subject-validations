from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..form_validators import ActivityAndFunctioningFormValidation


@tag('af')
class TestActivityAndFunctioningForm(TestCase):

    def test_flu_symptoms_yes_symptom_specify_required(self):
        cleaned_data = {
            'flu_symptoms': YES,
            'symptom_specify': None}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('symptom_specify', form_validator._errors)

    def test_flu_symptoms_yes_symptom_specified(self):
        cleaned_data = {
            'flu_symptoms': YES,
            'symptom_specify': 'cough'}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_flu_symptoms_no_symptom_specify_not_required(self):
        cleaned_data = {
            'flu_symptoms': NO,
            'symptom_specify': 'cough'}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('symptom_specify', form_validator._errors)

    def test_flu_symptoms_no_symptom_not_specified(self):
        cleaned_data = {
            'flu_symptoms': NO,
            'symptom_specify': None}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_mates_flu_symptoms_yes_mates_count_required(self):
        cleaned_data = {
            'housemate_flu_symptoms': YES,
            'housemates_with_flu_symptoms_count': None}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'housemates_with_flu_symptoms_count', form_validator._errors)

    def test_mates_flu_symptoms_yes_mates_count_specified(self):
        cleaned_data = {
            'housemate_flu_symptoms': YES,
            'housemates_with_flu_symptoms_count': 2}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_mates_flu_symptoms_no_mates_count_not_required(self):
        cleaned_data = {
            'housemate_flu_symptoms': NO,
            'housemates_with_flu_symptoms_count': 2}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn(
            'housemates_with_flu_symptoms_count', form_validator._errors)

    def test_mates_flu_symptoms_no_mates_count_not_specified(self):
        cleaned_data = {
            'housemate_flu_symptoms': NO,
            'housemates_with_flu_symptoms_count': None}
        form_validator = ActivityAndFunctioningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
