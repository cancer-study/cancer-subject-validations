from edc_constants.constants import YES
from edc_form_validators import FormValidator


class CurrentSymptomsFormValidation(FormValidator):

    def clean(self):
        required_fields = ['symptom_desc', 'patient_own_remedy', 'severity']
        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    YES,
                    field='any_worry',
                    field_required=required,
                )
