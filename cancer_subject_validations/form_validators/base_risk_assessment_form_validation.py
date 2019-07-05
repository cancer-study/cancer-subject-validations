from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessmentFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='tuberculosis',
            field_required='year_tb',
        )
