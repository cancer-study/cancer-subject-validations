from django.core.exceptions import ValidationError
from django.test import TestCase
from ..form_validators import BaseRiskAssessmentSmokingFormValidation


class TestBaseRiskAssessmentSmokingform(TestCase):

    def test_cigarette_smoking_valid(self):
        '''Assert raises if subject is smoking now,how many cigarettes
        per day does he/she smoke
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "cigarette_smoking": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cigarette_smoking', form_validator._errors)

    def test_cigarette_smokingy_invalid(self):
        '''Assert raises if subject is smoking now,how many cigarettes
        per day does he/she smoke
        '''
        cleaned_data = {
            "smoked_now": ' no, I used to smoke but quit',
            "cigarette_smoking": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cigarette_smoking_none(self):
        '''Assert raises if subject is smoking now,how many cigarettes
        per day does he/she smoke
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "cigarette_smoking": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cigarette_smoking_yes(self):
        '''Assert raises if subject is smoking now,how many cigarettes
        per day does he/she smoke
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "cigarette_smoking": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cigarette_smoking', form_validator._errors)

    def test_cigarette_smoking_years_smoked_invalid(self):
        '''Assert raises subject smokes.How many years has he/she smoked?
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "years_smoked": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('years_smoked', form_validator._errors)

    def test_cigarette_smoking_years_smoked_valid(self):
        '''Assert raises subject smokes.How many years has he/she smoked?
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "years_smoke": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cigarette_smoking_years_smoked_invalid_yes(self):
        '''Assert raises subject smokes.How many years has he/she smoked?
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "years_smoke": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cigarette_smoked_valid(self):
        '''Assert raises subject smokes.
        DON'T answer question about: How many cigarettes DID you smoke per day
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "cigarette_smoked": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cigarette_smoked', form_validator._errors)

    def test_cigarette_smoked_invalid(self):
        '''Assert raises subject smokes.
        DON'T answer question about: How many cigarettes DID you smoke per day
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "cigarette_smoked": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cigarette_smoked', form_validator._errors)

    def test_cigarette_smoked_valid_all(self):
        '''Assert raises subject smokes.
        DON'T answer question about: How many cigarettes DID you smoke per day
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "cigarette_smoked": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_when_quit_invalid_yes(self):
        '''Assert raises subject smokes. You cannot give info about quitting.
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "when_quit": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_when_quit_valid(self):
        '''Assert raises subject smokes. You cannot give info about quitting.
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "when_quit": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('when_quit', form_validator._errors)

    def test_when_quit_invalid(self):
        '''Assert raises subject smokes. You cannot give info about quitting.
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "when_quit": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_when_quit_invalid_response(self):
        '''Assert raises subject smokes. You cannot give info about quitting.
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "when_quit": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('when_quit', form_validator._errors)

    def test_years_smoked_before_valid(self):
        '''Assert raises subject smokes. must provide
        years_smoked_before
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "years_smoked_before": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('years_smoked_before', form_validator._errors)

    def test_years_smoked_before_invalid(self):
        '''True if subject smokes and provides years_smoked_before.
        '''
        cleaned_data = {
            "smoke_now": ' yes',
            "years_smoked_before": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_years_smoked_before_invalid_none(self):
        '''Assert raises subject smokes. You CANNOT give details about quitting.
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "years_smoked_before": '1',
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('years_smoked_before', form_validator._errors)

    def test_years_smoked_before_valid_none(self):
        '''True if subject does not smoke and
        does not give the years_smoked_before.
        '''
        cleaned_data = {
            "smoke_now": ' no, I used to smoke but quit',
            "years_smoked": None,
        }
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
