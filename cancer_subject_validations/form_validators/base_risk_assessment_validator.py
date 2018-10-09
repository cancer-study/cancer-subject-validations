from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessmentValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='tubercolosis',
            field_required='year_tb',
        )
