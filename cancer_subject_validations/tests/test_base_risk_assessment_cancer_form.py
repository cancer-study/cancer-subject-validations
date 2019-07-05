from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO, MALE, FEMALE
from ..form_validators import BaseRiskAssessementCancerFormValidator
from .models import SubjectConsent, SubjectVisit


class TestBaseRiskAssessmentCancerForm(TestCase):

    def setUp(self):
        BaseRiskAssessementCancerFormValidator.consent_cls = 'cancer_subject_validations.subjectconsent'
        self.subject_consent = SubjectConsent.objects.create(
            subject_identifier='11111111', screening_identifier='ABC12345',
            gender=MALE)

        self.subject_visit = SubjectVisit.objects.create(
            subject_identifier='11111111',)

    def test_family_cancer_type_yes_invalid(self):
        '''Assert raises if any relative has had any cancer but
        none is declared
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': YES,
            'family_cancer_type': None,
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
            'subject_visit': self.subject_visit,
            'family_cancer': NO,
            'family_cancer_type': 'blahblah',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('family_cancer_type', form_validator._errors)

    def test_family_cancer_type_valid(self):
        '''True if any relative has had any cancer,
        is yes and type defined
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': YES,
            'family_cancer_type': 'blahblah',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_family_cancer_type_no_valid(self):
        '''True if any relative has had any cancer,
        is no and none
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': NO,
            'family_cancer_type': None,
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_yes_invalid(self):
        '''Assert raises if the subject had previous cancer
        but did not specify previous cancer.
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'had_previous_cancer': YES,
            'previous_cancer': None,
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('previous_cancer', form_validator._errors)

    def test_had_previous_cancer_no_invalid(self):
        '''True if subject has had a previous cancer,
        is non and none
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'had_previous_cancer': NO,
            'previous_cancer': None,
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_yes_valid(self):
        '''True if subject has had a previous cancer,
        is yes and previous cancer is specified.
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'had_previous_cancer': YES,
            'previous_cancer': 'kln',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_family_cancer_type_male_invalid(self):
        '''Assert raises if any relative has had any cancer but
        none is declared
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': YES,
            'family_cancer_type': 'cervical_cancer',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('family_cancer_type', form_validator._errors)

    def test_family_cancer_type_male_valid(self):
        '''Assert raises if any relative has had any cancer but
        none is declared
        '''
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': YES,
            'family_cancer_type': 'esophageal_cancer',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_family_cancer_type_female_valid(self):
        '''Assert raises if any relative has had any cancer but
        none is declared
        '''
        self.subject_consent.gender = FEMALE
        self.subject_consent.save()
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'family_cancer': YES,
            'family_cancer_type': 'cervical_cancer',
        }
        form_validator = BaseRiskAssessementCancerFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
