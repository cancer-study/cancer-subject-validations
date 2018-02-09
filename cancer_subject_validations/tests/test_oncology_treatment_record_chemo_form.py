from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from edc_constants.constants import YES, NO


from ..form_validators import OncologyTreatmentRecordChemoFormValidation


class TestOncologyTreatmentRecordChemoFormValidation(TestCase):

    @tag('1')
    def test_chemo_delays_yes(self):
        """ why_delayed is required if chemo_delays
        is YES
         """
        cleaned_data = {'chemo_delays': YES,
                        'why_delayed': None}
        form_validator = OncologyTreatmentRecordChemoFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_chemo_delays_no(self):
        """ why_delayed is no required if chemo_delays
        is NO
         """
        cleaned_data = {'chemo_delays': NO,
                        'why_delayed': 'Explanation'}
        form_validator = OncologyTreatmentRecordChemoFormValidation(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('why_delayed'))

    @tag('1')
    def test_chemo_reduced_yes(self):
        """ why_reduced is required if chemo_reduced
        is YES
         """
        cleaned_data = {'chemo_reduced': YES,
                        'why_reduced': None}
        form_validator = OncologyTreatmentRecordChemoFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_chemo_reduced_no(self):
        """ why_reduced is no required if chemo_reduced
        is NO
         """
        cleaned_data = {'chemo_reduced': NO,
                        'why_reduced': 'Explanation'}
        form_validator = OncologyTreatmentRecordChemoFormValidation(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('why_delayed'))
