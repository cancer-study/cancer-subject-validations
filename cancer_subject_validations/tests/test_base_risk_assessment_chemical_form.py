from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO

from ..form_validators import BaseRiskAssessmentChemicalFormValidation


class TestBaseRiskAssessmentChemicalFormValidation(TestCase):

    def test_asbestos_yes_none_protection(self):
        """ Asserts asbestos_no_protection is required if asbestos is YES.
        """
        cleaned_data = {'asbestos': YES,
                        'asbestos_no_protection': None}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_asbestos_yes_with_protection(self):
        """ Asserts asbestos_no_protection is required if asbestos is YES.
        """
        cleaned_data = {'asbestos': YES,
                        'asbestos_no_protection': '<5 years'}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_asbestos_no_with_protection(self):
        """ Asserts asbestos_no_protection  is no required if asbestos is NO.
        """
        cleaned_data = {'asbestos': NO,
                        'asbestos_no_protection': 'Explanation'}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_asbestos_no_none_protection(self):
        """ Asserts asbestos_no_protection  is no required if asbestos is NO.
        """
        cleaned_data = {'asbestos': NO,
                        'asbestos_no_protection': None}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_chemicals_yes_no_chem_time(self):
        """ Asserts chemicals_time is required if chemicals is YES.
        """
        cleaned_data = {'chemicals': YES,
                        'chemicals_time': None}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_chemicals_yes_chem_time(self):
        """ Asserts chemicals_time is required if chemicals is YES.
        """
        cleaned_data = {'chemicals': YES,
                        'chemicals_time': get_utcnow()}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_chemicals_no_with_chem_time(self):
        """ Asserts chemicals_time is no required if chemicals is NO.
        """
        cleaned_data = {'chemicals': NO,
                        'chemicals_time': get_utcnow()}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_arsenic_smelting_yes_no_protect_time(self):
        """ Asserts total_no_protection is required if arsenic_smelting is YES.
        """
        cleaned_data = {'arsenic_smelting': YES,
                        'total_time_no_protection': None}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_arsenic_smelting_yes_with_protect_time(self):
        """ Asserts total_no_protection is required if arsenic_smelting is YES.
        """
        cleaned_data = {'arsenic_smelting': YES,
                        'total_time_no_protection': get_utcnow()}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.clean()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arsenic_smelting_no_protect_time(self):
        """ Asserts total_time_no_protection is no required if arsenic_smelting
            is NO.
        """
        cleaned_data = {'arsenic_smelting': NO,
                        'total_time_no_protection': 'Explanation'}
        form_validator = BaseRiskAssessmentChemicalFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
