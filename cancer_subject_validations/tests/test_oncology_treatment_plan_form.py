from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import OncologyTreatmentPlanFormValidation


class TestOncologyTreatmentPlanForm(TestCase):

    def test_treatment_plan_yes_chemo_required(self):
        '''Asserts raises exception for required field chemotherapy missing
        if treatment plan yes.'''

        cleaned_data = {
            'treatment_plan': YES,
            'chemotherapy': None,
            'radiation_plan': YES,
            'surgical_plan': YES}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemotherapy', form_validator._errors)

    def test_treatment_plan_yes_radiation_plan_required(self):
        '''Asserts raises exception for required field radiation plan missing
        if treatment plan yes.'''

        cleaned_data = {
            'treatment_plan': YES,
            'chemotherapy': NO,
            'radiation_plan': None,
            'surgical_plan': YES}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('radiation_plan', form_validator._errors)

    def test_treatment_plan_yes_surgical_plan_required(self):
        '''Asserts raises exception for required field surgical plan missing
        if treatment plan yes.'''

        cleaned_data = {
            'treatment_plan': YES,
            'chemotherapy': YES,
            'radiation_plan': NO,
            'surgical_plan': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('surgical_plan', form_validator._errors)

    def test_treatment_plan_yes_chemo_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'treatment_plan': YES,
            'chemotherapy': NO,
            'radiation_plan': YES,
            'surgical_plan': NO}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_treatment_plan_no_chemo_invalid(self):
        '''Asserts raises exception chemotherapy provided but not required
        for treatment plan no.'''

        cleaned_data = {
            'treatment_plan': NO,
            'chemotherapy': YES,
            'radiation_plan': None,
            'surgical_plan': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemotherapy', form_validator._errors)

    def test_treatment_plan_no_radiation_plan_invalid(self):
        '''Asserts raises exception radiation plan provided but not required
        for treatment plan no.'''

        cleaned_data = {
            'treatment_plan': NO,
            'chemotherapy': None,
            'radiation_plan': YES,
            'surgical_plan': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('radiation_plan', form_validator._errors)

    def test_treatment_plan_no_surgical_plan_invalid(self):
        '''Asserts raises exception surgical plan provided but not required
        for treatment plan no.'''

        cleaned_data = {
            'treatment_plan': NO,
            'chemotherapy': None,
            'radiation_plan': None,
            'surgical_plan': NO}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('surgical_plan', form_validator._errors)

    def test_treatment_plan_no_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'treatment_plan': NO,
            'chemotherapy': None,
            'radiation_plan': None,
            'surgical_plan': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_chemotherapy_yes_chemo_intent_required(self):
        '''Asserts raises exception for required field chemo intent missing
        if chemotherapy yes.'''

        cleaned_data = {
            'chemotherapy': YES,
            'chemo_intent': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemo_intent', form_validator._errors)

    def test_chemotherapy_yes_chemo_intent_provided(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'chemotherapy': YES,
            'chemo_intent': 'adjuvant'}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_chemotherapy_no_chemo_intent_invalid(self):
        '''Asserts raises exception for non-required field chemo intent
        provided if chemotherapy no.'''

        cleaned_data = {
            'chemotherapy': NO,
            'chemo_intent': 'standard'}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('chemo_intent', form_validator._errors)

    def test_chemotherapy_no_chemo_intent_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'chemotherapy': NO,
            'chemo_intent': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_surgical_plan_yes_planned_operation_required(self):
        '''Asserts raises exception for required field planned operation missing
        if surgical plan yes.'''

        cleaned_data = {
            'surgical_plan': YES,
            'planned_operation': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('planned_operation', form_validator._errors)

    def test_surgical_plan_yes_planned_operation_provided(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'surgical_plan': YES,
            'planned_operation': 'double mastectomy, oopherectomy.'}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_surgical_plan_no_planned_operation_invalid(self):
        '''Asserts raises exception for non-required field planned operation
        provided if surgical plan no.'''

        cleaned_data = {
            'surgical_plan': NO,
            'planned_operation': 'double mastectomy, oopherectomy.'}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('planned_operation', form_validator._errors)

    def test_surgical_plan_no_planned_operation_valid(self):
        '''Tests cleaned data validates, or fails tests if exception
        unexpectedly raised.'''

        cleaned_data = {
            'surgical_plan': NO,
            'planned_operation': None}
        form_validator = OncologyTreatmentPlanFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
