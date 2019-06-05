from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..form_validators import CurrentSymptomsFormValidation


@tag('curr')
class TestCurrentSymptomsForm(TestCase):

    def test_current_symptoms_invalid(self):
        '''Assert raises if the patient is
        worried and does not give desc.
        '''
        cleaned_data = {
            "any_worry": YES,
            "symptom_desc": None,
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('symptom_desc', form_validator._errors)

    def test_current_symptoms_valid(self):
        '''True if patient is worried and desc is
        given
        '''
        cleaned_data = {
            "any_worry": YES,
            "symptom_desc": 'ill',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_current_symptoms_invalid_no(self):
        '''Assert raises if patient is not worried but
        provides a desc.
        '''
        cleaned_data = {
            "any_worry": NO,
            "symptom_desc": 'ill',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('symptom_desc', form_validator._errors)

    def test_current_symptoms_valid_no(self):
        '''True if the patient is not worried and
        has no desc.
        '''
        cleaned_data = {
            "any_worry": NO,
            "severity": 'NOT_APPLICABLE',
            "symptom_desc": None,
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_own_remedy_invalid(self):
        '''Assert raises if patient is worried and
        does not specify the remedy he/she took.
        '''
        cleaned_data = {
            "any_worry": YES,
            "patient_own_remedy": None,
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('patient_own_remedy', form_validator._errors)

    def test_patient_own_remedy_valid(self):
        '''True if patient is worried and provides
        the remedy he/she took.
        '''
        cleaned_data = {
            "any_worry": YES,
            "patient_own_remedy": 'medic',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_own_remedy_valid_no(self):
        '''True if patient is not worried and does
        not have a remedy.
        '''
        cleaned_data = {
            "any_worry": NO,
            "severity": 'NOT_APPLICABLE',
            "patient_own_remedy": None,
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_patient_own_remedy_invalid_no(self):
        '''Assert raises if patient is not worried, but
        give a remedy taken.
        '''
        cleaned_data = {
            "any_worry": NO,
            "patient_own_remedy": 'medic',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('patient_own_remedy', form_validator._errors)

    def test_severity_invalid(self):
        '''Assert raises if the patient is worried but
        did not specify how severe.
        '''
        cleaned_data = {
            "any_worry": YES,
            "severity": 'NOT_APPLICABLE',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('severity', form_validator._errors)

    @tag('at')
    def test_severity_valid(self):
        '''True if patient is worried and provides
        the level of severity.
        '''
        cleaned_data = {
            "any_worry": YES,
            "severity": 'mild',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_severity_valid_no(self):
        '''True if patient is not worried and has no
        severe levels.
        '''
        cleaned_data = {
            "any_worry": NO,
            "severity": 'NOT_APPLICABLE',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_severity_invalid_no(self):
        '''Assert raises if patient is not worried but
        provides a severe level.
        '''
        cleaned_data = {
            "any_worry": NO,
            "severity": 'mild',
        }
        form_validator = CurrentSymptomsFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('severity', form_validator._errors)
