from django.core.exceptions import ValidationError

from django.test import TestCase, tag


from ..constants.lab_result_tb_form_constants import (
    YES_ISONIAZID_PREVENTATIVE_THERAPY, YES_COMBINATION_ANTI_TB)


from ..form_validators import LabResultTbFormValidation


class TestLabTbResultFormValidation(TestCase):

    @tag('1')
    def test_tb_details(self):
        """ tb_treatment_start is required if tb_treatment
        is 'Yes, isoniazid preventative therapy (IPT)'
         """
        cleaned_data = {'tb_treatment':
                        YES_ISONIAZID_PREVENTATIVE_THERAPY,
                        'tb_treatment_start': None}
        form_validator = LabResultTbFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_tb_details2(self):
        """ tb_treatment_start is required if tb_treatment
        is 'Yes, combination anti-tuberculosis treatment (ATT)'
         """
        cleaned_data = {'tb_treatment':
                        YES_COMBINATION_ANTI_TB,
                        'tb_treatment_start': None}
        form_validator = LabResultTbFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
