from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..form_validators import BaseRiskAssessementCancerFormValidator


@tag('c')
class TestBaseRiskAssessmentCancerForm(TestCase):

    pass
#     def test_family_cancer_type_yes_invalid(self):
#         cleaned_data = {
#             "family_cancer": YES,
#             "family_cancer_type": None,
#         }
#         form_validator = BaseRiskAssessementCancerFormValidator(
#             cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form_validator.validate)
#         self.assertIn('family_cancer_type', form_validator._errors)
#
#     def test_family_cancer_type_no_invalid(self):
#         cleaned_data = {
#             "family_cancer": NO,
#             "family_cancer_type": 'blahblah',
#         }
#         form_validator = BaseRiskAssessementCancerFormValidator(
#             cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form_validator.validate)
#         print(form_validator._errors)
#         self.assertIn('family_cancer_type', form_validator._errors)

#     def test_family_cancer_type_valid(self):
#         cleaned_data = {
#             "family_cancer": YES,
#             "family_cancer_type": 'blahblah',
#         }
#         form_validator = BaseRiskAssessementCancerFormValidator(
#             cleaned_data=cleaned_data)
#         try:
#             form_validator.validate()
#         except ValidationError as e:
#             self.fail(f'ValidationError unexpectedly raised. Got{e}')

#     def test_family_cancer_type_no_valid(self):
#         cleaned_data = {
#             "family_cancer": NO,
#             "family_cancer_type": None,
#         }
#         form_validator = BaseRiskAssessementCancerFormValidator(
#             cleaned_data=cleaned_data)
#         try:
#             form_validator.validate()
#         except ValidationError as e:
#             self.fail(f'ValidationError unexpectedly raised. Got{e}')
