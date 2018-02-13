from edc_form_validators import FormValidator
from edc_constants.constants import YES


class BaseRiskAssessmentCancerFormValidation(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='family_cancer',
            field_required='family_cancer_type',
            required_msg=(
                'If any relative has had any cancer, what type was it?')
        )

        self.required_if(
            YES,
            field='had_previous_cancer',
            field_required='previous_cancer',
            required_msg=('If subject has had a previous cancer, '
                          'what kind of cancer was it')
        )

        return self.cleaned_data
