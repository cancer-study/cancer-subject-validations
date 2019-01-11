from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessmentSmokingFormValidation(FormValidator):

    def clean(self):
        required_fields = ['cigarette_smoking', 'years_smoked',
                           'cigarette_smoked', 'when_quit',
                           'years_smoked_before']
        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    YES,
                    field='smoke_now',
                    field_required=required
                )
