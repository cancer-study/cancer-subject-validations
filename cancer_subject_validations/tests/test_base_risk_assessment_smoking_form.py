from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO

from ..form_validators import BaseRiskAssessmentSmokingFormValidation


class TestBaseRiskAssessmentSmokingFormValidation(TestCase):

    def test_yes_smoking_none_smoking_something(self):
        """ cigarette_smoking is required if smoke_now is YES.
        """
        cleaned_data = {'smoke_now': YES,
                        'cigarette_smoking': '14 or fewer cigarettes a day',
                        'years_smoked': 8}
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_yes_smoking_without_smoking_something(self):
        """ cigarette_smoking is required if smoke_now is YES.
        """
        cleaned_data = {'smoke_now': YES,
                        'cigarette_smoking': None}
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_smoking_details_no_with_smoking_something(self):
        """ cigarette_smoking is no required if smoke_now is NO.
        """
        cleaned_data = {'smoke_now': NO,
                        'cigarette_smoking': '14 or fewer cigarettes a day'}
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_smoking_details_yes_with_years_smoked(self):
        """ years_smoked is required if smoke_now is YES.
        """
        cleaned_data = {'smoke_now': YES,
                        'years_smoked': None}
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_smoking_details_no_yes_years_smoked(self):
        """ years_smoked is no required if smoke_now
        is NO
         """
        cleaned_data = {'smoke_now': NO,
                        'years_smoked': 5}
        form_validator = BaseRiskAssessmentSmokingFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

#     @tag('1')
#     def test_smoking_details_yes3(self):
#         """ cigarette_smoked is required if smoke_now
#         is YES
#          """
#         cleaned_data = {'smoke_now': YES,
#                         'cigarette_smoked': 'something'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form_validator.clean)
#
#     @tag('1')
#     def test_smoking_details_no3(self):
#         """ cigarette_smoked is no required if smoke_now
#         is NO
#          """
#         cleaned_data = {'smoke_now': NO,
#                         'cigarette_smoked': 'Explanation'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertIsNone(form_validator._errors.get(
#             'cigarette_smoked'))
#
#     @tag('1')
#     def test_smoking_details_yes4(self):
#         """ when_quit is required if smoke_now
#         is YES
#          """
#         cleaned_data = {'smoke_now': YES,
#                         'when_quit': 'something'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form_validator.clean)
#
#     @tag('1')
#     def test_smoking_details_no4(self):
#         """ when_quit is no required if smoke_now
#         is NO
#          """
#         cleaned_data = {'smoke_now': NO,
#                         'when_quit': 'Explanation'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertIsNone(form_validator._errors.get(
#             'when_quit'))
#
#     @tag('1')
#     def test_smoking_details_yes5(self):
#         """ years_smoked_before is required if smoke_now
#         is YES
#          """
#         cleaned_data = {'smoke_now': YES,
#                         'years_smoked_before': 'something'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form_validator.clean)
#
#     @tag('1')
#     def test_smoking_details_no5(self):
#         """ years_smoked_before is no required if smoke_now
#         is NO
#          """
#         cleaned_data = {'smoke_now': NO,
#                         'years_smoked_before': 'Explanation'}
#         form_validator = BaseRiskAssessmentSmokingFormValidation(
#             cleaned_data=cleaned_data)
#         self.assertIsNone(form_validator._errors.get(
#             'years_smoked_before'))
