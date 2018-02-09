from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES


from ..form_validators import MainCancerDiagnosisFormValidaton


class TestMainCancerDiagnosisFormValidaton(TestCase):

    @tag('1')
    def test_diagnosis_details(self):
        """ cancer_category is required if diagnosis
        is YES
         """
        cleaned_data = {'diagnosis': YES,
                        'cancer_category': 'Explanation'}
        form_validator = MainCancerDiagnosisFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details2(self):
        """ date_diagnosed is required if diagnosis
        is YES
         """
        cleaned_data = {'diagnosis': YES,
                        'date_diagnosed': 'date'}
        form_validator = MainCancerDiagnosisFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details3(self):
        """ diagnosis_basis is required if diagnosis
        is YES
         """
        cleaned_data = {'diagnosis': YES,
                        'diagnosis_basis': 'Explanation'}
        form_validator = MainCancerDiagnosisFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details4(self):
        """ diagnosis_word is required if diagnosis
        is YES
         """
        cleaned_data = {'diagnosis': YES,
                        'diagnosis_word': 'Explanation'}
        form_validator = MainCancerDiagnosisFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_diagnosis_details5(self):
        """ cancer_site is required if diagnosis
        is YES
         """
        cleaned_data = {'diagnosis': YES,
                        'cancer_site': 'Explanation'}
        form_validator = MainCancerDiagnosisFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
