from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..form_validators import BaseRiskAssessmentChemicalValidation
from django.core.exceptions import ValidationError
from edc_base.utils import get_utcnow


@tag('1')
class TestBaseRiskAssessmentForm(TestCase):
    def test_abestos_yes(self):
        cleaned_data = {
            "abestos": YES,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abestos_no(self):
        cleaned_data = {
            "abestos": NO,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abestos_no_error(self):
        cleaned_data = {
            "abestos": NO,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abestos_valid(self):
        cleaned_data = {
            "abestos": YES,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_chemicals_yes(self):
        cleaned_data = {
            "other_chemicals": YES,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('how_long', form_validator._errors)

    def test_other_chemicals_no(self):
        cleaned_data = {
            "other_chemicals": NO,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('how_long', form_validator._errors)

    def test_other_chemicals_no_error(self):
        cleaned_data = {
            "other_chemicals": NO,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_other_chemicals_valid(self):
        cleaned_data = {
            "other_chemicals": YES,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arsenic_smelting_yes(self):
        cleaned_data = {
            "arsenic_smelting": YES,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(

            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('how_long', form_validator._errors)

    def test_arsenic_smelting_no(self):
        cleaned_data = {
            "arsenic_smelting": NO,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('how_long', form_validator._errors)

    def test_arsenic_smelting_no_error(self):
        cleaned_data = {
            "arsenic_smelting": NO,
            "how_long": None,
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_arsenic_smelting_valid(self):
        cleaned_data = {
            "arsenic_smelting": YES,
            "how_long": get_utcnow(),
            }
        form_validator = BaseRiskAssessmentChemicalValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
