from edc_form_validators import FormValidator
from edc_constants.constants import YES


class BaseRiskAssessmentSmokingFormValidation(FormValidator):

    def clean(self):

        field_required_list = ['years_smoked', 'cigarette_smoking']

        for required in field_required_list:
            self.required_if(
                YES,
                field='smoke_now',
                field_required=required
            )

            return self.cleaned_data
