from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class BaseRiskAssessmentCancerFormValidation(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='family_cancer',
            field_required='family_cancer_type',
        )

        self.required_if(
            YES,
            field='had_previous_cancer',
            field_required='previous_cancer',
        )

        return self.cleaned_data
