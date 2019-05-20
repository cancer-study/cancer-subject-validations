from _datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import (YES, NO, NEG, POS)

from ..form_validators import SymptomsAndTestingFormValidator


@tag('sat')
class TestSymptomsAndTestingForm(TestCase):

    def test_hiv_tested_yes_hiv_result_required(self):
        cleaned_data = {
            'hiv_tested': YES,
            'hiv_test_result': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('hiv_test_result', form_validator._errors)

    def test_hiv_tested_yes_hiv_result_provided(self):
        cleaned_data = {
            'hiv_tested': YES,
            'hiv_test_result': NEG,
            'neg_date': get_utcnow().date() - timedelta(days=30)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_hiv_tested_no_hiv_result_invalid(self):
        cleaned_data = {
            'hiv_tested': NO,
            'hiv_test_result': NEG,
            'hiv_result': NEG
        }
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('hiv_test_result', form_validator._errors)

    def test_hiv_tested_no_hiv_result_valid(self):
        cleaned_data = {
            'hiv_tested': NO,
            'hiv_test_result': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_hiv_test_result_neg_negative_date_required(self):
        cleaned_data = {
            'hiv_test_result': NEG,
            'neg_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('neg_date', form_validator._errors)

    def test_hiv_test_result_neg_negative_date_provided(self):
        cleaned_data = {
            'hiv_test_result': NEG,
            'neg_date': get_utcnow().date() - timedelta(days=30)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_hiv_test_result_pos_positive_date_required(self):
        cleaned_data = {
            'hiv_test_result': POS,
            'pos_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('pos_date', form_validator._errors)

    def test_hiv_test_result_pos_positive_date_provided(self):
        cleaned_data = {
            'hiv_test_result': POS,
            'pos_date': get_utcnow().date() - timedelta(days=30)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_hiv_test_result_neg_pos_date_invalid(self):
        cleaned_data = {
            'hiv_test_result': NEG,
            'neg_date': get_utcnow().date(),
            'pos_date': get_utcnow().date() - timedelta(days=10)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('pos_date', form_validator._errors)

    def test_hiv_test_result_neg_pos_date_valid(self):
        cleaned_data = {
            'hiv_test_result': NEG,
            'neg_date': get_utcnow().date(),
            'pos_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_hiv_test_result_pos_neg_date_invalid(self):
        cleaned_data = {
            'hiv_test_result': POS,
            'neg_date': get_utcnow().date(),
            'pos_date': get_utcnow().date() - timedelta(days=10)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('neg_date', form_validator._errors)

    def test_hiv_test_result_pos_neg_date_valid(self):
        cleaned_data = {
            'hiv_test_result': POS,
            'neg_date': None,
            'pos_date': get_utcnow().date()}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_arv_art_therapy_yes_arv_art_start_required(self):
        cleaned_data = {
            'arv_art_therapy': YES,
            'arv_art_start_date': None,
            'arv_art_now': YES}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arv_art_start_date', form_validator._errors)

    def test_arv_art_therapy_yes_arv_art_start_provided(self):
        cleaned_data = {
            'arv_art_therapy': YES,
            'arv_art_start_date': get_utcnow().date(),
            'arv_art_now': YES}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_arv_art_therapy_no_arv_art_start_invalid(self):
        cleaned_data = {
            'arv_art_therapy': NO,
            'arv_art_start_date': get_utcnow().date(),
            'arv_art_now': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arv_art_start_date', form_validator._errors)

    def test_arv_art_therapy_no_arv_art_now_invalid(self):
        cleaned_data = {
            'arv_art_therapy': NO,
            'arv_art_start_date': None,
            'arv_art_now': YES}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('arv_art_now', form_validator._errors)

    def test_arv_art_therapy_no_valid(self):
        cleaned_data = {
            'arv_art_therapy': NO,
            'arv_art_start_date': None,
            'arv_art_now': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_arv_art_therapy_no_stop_date_valid(self):
        cleaned_data = {
            'arv_art_therapy': NO,
            'arv_art_start_date': None,
            'arv_art_now': None,
            'art_art_stop_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_arv_art_therapy_no_stop_date_invalid(self):
        cleaned_data = {
            'arv_art_therapy': NO,
            'arv_art_start_date': None,
            'arv_art_now': None,
            'art_art_stop_date': get_utcnow().date() - timedelta(days=90)}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('art_art_stop_date', form_validator._errors)

    def test_arv_art_now_no_stop_date_required(self):
        cleaned_data = {
            'arv_art_now': NO,
            'art_art_stop_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('art_art_stop_date', form_validator._errors)

    def test_arv_art_now_no_stop_date_provided(self):
        cleaned_data = {
            'arv_art_now': NO,
            'art_art_stop_date': get_utcnow().date()}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_arv_art_now_yes_stop_date_invalid(self):
        cleaned_data = {
            'arv_art_now': YES,
            'art_art_stop_date': get_utcnow().date()}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('art_art_stop_date', form_validator._errors)

    def test_arv_art_now_yes_stop_date_valid(self):
        cleaned_data = {
            'arv_art_now': YES,
            'art_art_stop_date': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_facility_first_seen_other_required(self):
        cleaned_data = {
            'facility_first_seen': '00-0-00',
            'facility_first_seen_other': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('facility_first_seen_other', form_validator._errors)

    def test_facility_first_seen_other_provided(self):
        cleaned_data = {
            'facility_first_seen': '00-0-00',
            'facility_first_seen_other': 'cancer'}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_facility_first_seen_different(self):
        cleaned_data = {
            'facility_first_seen': '00-0-11',
            'facility_first_seen_other': None}
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')

    def test_pos_test_valid(self):
        cleaned_data = {
            'hiv_tested': YES,
            'hiv_test_result': POS,
            'pos_date': get_utcnow().date(),
            'hiv_result': 'Pos',
            'arv_art_therapy': NO
        }
        form_validator = SymptomsAndTestingFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError raised unexpectedly. Got{e}')
