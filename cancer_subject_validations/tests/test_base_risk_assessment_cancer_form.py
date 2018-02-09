from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO

from ..form_validators import BaseRiskAssessmentCancerFormValidation


class TestBaseRiskAssessmentCancerFormValidation(TestCase):

    def test_family_cancer_yes_none_type(self):
        """ family_cancer_type is required if family_cancer is YES.
        """
        cleaned_data = {'family_cancer': YES,
                        'family_cancer_type': None}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_family_cancer_yes_with_type(self):
        """ family_cancer_type is required if family_cancer is YES.
        """
        cleaned_data = {'family_cancer': YES,
                        'family_cancer_type': 'Breast cancer'}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_family_cancer_no(self):
        """ family_cancer_type  is no required if family_cancer is NO.
        """
        cleaned_data = {'family_cancer': NO,
                        'family_cancer_type': 'Breast cancer'}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_family_cancer_no_none_type(self):
        """ family_cancer_type  is no required if family_cancer is NO.
        """
        cleaned_data = {'family_cancer': NO,
                        'family_cancer_type': None}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_had_previous_cancer_yes_none_previous(self):
        """ previous_cancer is required if had_previous_cancer is YES.
        """
        cleaned_data = {'had_previous_cancer': YES,
                        'previous_cancer': None}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_had_previous_cancer_yes_with_previous(self):
        """ previous_cancer is required if had_previous_cancer is YES.
        """
        cleaned_data = {'had_previous_cancer': YES,
                        'previous_cancer': 'Breast cancer'}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_previous_cancer_no_with_previous(self):
        """previous_cancer  is no required if had_previous_cancer is NO.
        """
        cleaned_data = {'had_previous_cancer': NO,
                        'previous_cancer': 'Lymphoma'}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_previous_cancer_no_none_previous(self):
        """previous_cancer  is no required if had_previous_cancer is NO.
        """
        cleaned_data = {'had_previous_cancer': NO,
                        'previous_cancer': None}
        form_validator = BaseRiskAssessmentCancerFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
