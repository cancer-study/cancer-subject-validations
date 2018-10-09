from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessementCancerFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='family_cancer',
            field_required='family_cancer_type',
        )
