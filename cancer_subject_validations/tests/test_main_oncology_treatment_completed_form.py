from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES


from ..form_validators import MainOncologyTreatmentCompletedFormValidation


class TestMainOncologyTreatmentPlanCompletedValidaton(TestCase):

    @tag('1')
    def test_treatment_completion_details(self):
        """ treatment_detail is required if patient_had_chemo
        is YES
         """
        cleaned_data = {'patient_had_chemo': YES,
                        'treatment_detail': None}
        form_validator = MainOncologyTreatmentCompletedFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_treatment_completion_details2(self):
        """ treatment_detail is required if patient_had_radiation
        is YES
         """
        cleaned_data = {'patient_had_radiation': YES,
                        'treatment_detail': None}
        form_validator = MainOncologyTreatmentCompletedFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_treatment_completion_details3(self):
        """ patient_had_surgery is required if treatment_detail
        is YES
         """
        cleaned_data = {'patient_had_surgery': YES,
                        'treatment_detail': None}
        form_validator = MainOncologyTreatmentCompletedFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
