from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO

from ..form_validators import (
    OncologyTreatmentRecordRadiationFormValidation)


class TestOncologyTreatmentRecordRadiationFormValidation(TestCase):

    @tag('1')
    def test_radiation_details_yes1(self):
        """ amount_radiation is not required if radiation_details
        is YES
         """
        cleaned_data = {'radiation_details': YES,
                        'amount_radiation': '01'}
        form_validator = OncologyTreatmentRecordRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_radiation_details_yes2(self):
        """ concomitant is not required if radiation_details
        is YES
         """
        cleaned_data = {'radiation_details': YES,
                        'concomitant': 'something'}
        form_validator = OncologyTreatmentRecordRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_radiation_details_no1(self):
        """ amount_radiation is required if radiation_details
        is NO
         """
        cleaned_data = {'radiation_details': NO,
                        'amount_radiation': None}
        form_validator = OncologyTreatmentRecordRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertFalse(form_validator._errors.get('amount_radiation'))
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_radiation_details_no2(self):
        """ concomitant is required if radiation_details
        is NO
         """
        cleaned_data = {'radiation_details': NO,
                        'concomitant': None}
        form_validator = OncologyTreatmentRecordRadiationFormValidation(
            cleaned_data=cleaned_data)
        self.assertFalse(form_validator._errors.get('concomitant'))
        self.assertRaises(ValidationError, form_validator.clean)
