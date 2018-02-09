from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES, NO


from ..form_validators import MainSymptomsAndTestingFormValidaton


class TestMainSymptomsAndTestingFormValidation(TestCase):

    @tag('1')
    def test_symptom_details_yes1(self):
        """ hiv_test_result is required if hiv_tested
        is YES
         """
        cleaned_data = {'hiv_tested': YES,
                        'hiv_test_result': None}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes2(self):
        """ neg_date is not required if hiv_tested
        is NO
         """
        cleaned_data = {'hiv_test_result': NO,
                        'neg_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('neg_date'))

    @tag('1')
    def test_symptom_details_yes3(self):
        """ pos_date is not required if hiv_tested
        is NO
         """
        cleaned_data = {'hiv_test_result': NO,
                        'pos_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('pos_date'))

    @tag('1')
    def test_symptom_details_yes4(self):
        """ hiv_test_result is required if hiv_test_result
        is YES
         """
        cleaned_data = {'hiv_test_result': YES,
                        'pos_date': None}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes5(self):
        """ hiv_test_result is not required if hiv_tested
        is POS
         """
        cleaned_data = {'hiv_test_result': 'POS',
                        'neg_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('neg_date'))

    @tag('1')
    def test_symptom_details_yes6(self):
        """ hiv_test_result is not required if hiv_tested
        is NO
         """
        cleaned_data = {'hiv_tested': NO,
                        'hiv_test_result': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('hiv_test_result'))

    @tag('1')
    def test_symptom_details_yes7(self):
        """ pos_date is not required if hiv_tested
        is NO
         """
        cleaned_data = {'hiv_tested': NO,
                        'pos_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('pos_date'))

    @tag('1')
    def test_symptom_details_yes8(self):
        """ arv_art_therapy is required if arv_art_start_date
        is YES
         """
        cleaned_data = {'arv_art_start_date': YES,
                        'arv_art_therapy': None}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes9(self):
        """ arv_art_now is required if arv_art_therapy
        is YES
         """
        cleaned_data = {'arv_art_therapy': YES,
                        'arv_art_now': None}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_symptom_details_yes10(self):
        """ arv_art_start_date is not required if arv_art_start_date
        is NO
         """
        cleaned_data = {'arv_art_therapy': NO,
                        'arv_art_start_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('arv_art_start_date'))

    @tag('1')
    def test_symptom_details_yes11(self):
        """ arv_art_stop_date is not required if arv_art_start_date
        is NO
         """
        cleaned_data = {'arv_art_therapy': NO,
                        'arv_art_stop_date': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('arv_art_stop_date'))

    @tag('1')
    def test_symptom_details_yes12(self):
        """ arv_art_now is not required if arv_art_start_date
        is YES
         """
        cleaned_data = {'arv_art_stop_date': YES,
                        'arv_art_now': 'status'}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('arv_art_now'))

    @tag('1')
    def test_symptom_details_yes13(self):
        """ arv_art_now is required if arv_art_stop_date
        is NO
         """
        cleaned_data = {'arv_art_therapy': YES,
                        'arv_art_now': None}
        form_validator = MainSymptomsAndTestingFormValidaton(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
