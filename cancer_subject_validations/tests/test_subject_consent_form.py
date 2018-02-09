from django.core.exceptions import ValidationError
from django.test import TestCase, tag

from edc_constants.constants import YES, NO

from ..form_validators import SubjectConsentFormValidation


class TestSubjectConsentFormValidation(TestCase):

    @tag('1')
    def test_unconcious_yes(self):
        """ guadian_name is required if unconcious
        is YES
         """
        cleaned_data = {'unconcious': YES,
                        'guadian_name': None}
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_unconcious_no(self):
        """ guadian_name is no required if unconcious
        is NO
         """
        cleaned_data = {'unconcious': NO,
                        'guadian_name': 'Explanation'}
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('guadian_name'))

    @tag('1')
    def test_abnormal_mind_yes(self):
        """ guadian_name is required if abnormal_mind
        is YES
         """
        cleaned_data = {'abnormal_mind': YES,
                        'guadian_name': None}
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)

    @tag('1')
    def test_abnormal_mind_no(self):
        """ guadian_name is no required if abnormal_mind
        is NO
         """
        cleaned_data = {'abnormal_mind': NO,
                        'guadian_name': 'Explanation'}
        form_validator = SubjectConsentFormValidation(
            cleaned_data=cleaned_data)
        self.assertIsNone(form_validator._errors.get('guadian_name'))
