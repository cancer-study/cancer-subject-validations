from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES


from ..form_validators import MainOncologyTreatmentPlanFormValidaton


class TestMainOncologyTreatmentPlanFormValidaton(TestCase):

    @tag('1')
    def test_treatment_details(self):
        """ chemotherapy is required if treatment_plan
        is YES
         """
        cleaned_data = {'treatment_plan': YES,
                        'chemotherapy': 'Explanation'}
        form_validator = MainOncologyTreatmentPlanFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details2(self):
        """ radiation_plan is required if treatment_plan
        is YES
         """
        cleaned_data = {'treatment_plan': YES,
                        'radiation_plan': 'Explanation'}
        form_validator = MainOncologyTreatmentPlanFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details3(self):
        """ surgical_plan is required if treatment_plan
        is YES
         """
        cleaned_data = {'treatment_plan': YES,
                        'surgical_plan': 'Explanation'}
        form_validator = MainOncologyTreatmentPlanFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
