from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..form_validators import BaseRiskAssessmentFemaleValidation
from django.core.exceptions import ValidationError


class TestBaseRiskAssessmentChemicalForm(TestCase):

    @tag('22')
    def test_breastfed_with_children(self):
        options = {
            'children': 0,
            'years_breastfed': 2
        }
        form = BaseRiskAssessmentFemaleValidation(
            cleaned_data=options)
        self.assertRaises(ValidationError, form.validate)
