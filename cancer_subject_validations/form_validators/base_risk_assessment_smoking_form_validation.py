from edc_form_validators import FormValidator


class BaseRiskAssessmentSmokingFormValidation(FormValidator):

    def clean(self):

        self.required_if(
            ' yes',
            field='smoke_now',
            field_required='cigarette_smoking'
        )

        self.required_if(
            ' yes',
            field='smoke_now',
            field_required='years_smoked'
        )

        required_fields = ['cigarette_smoked', 'when_quit',
                           'years_smoked_before']
        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    ' no, I used to smoke but quit',
                    field='smoke_now',
                    field_required=required)
