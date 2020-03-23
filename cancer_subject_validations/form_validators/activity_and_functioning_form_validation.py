from edc_constants.constants import YES
from edc_form_validators import FormValidator


class ActivityAndFunctioningFormValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='flu_symptoms',
            field_required='symptom_specify')

        self.required_if(
            YES,
            field='housemate_flu_symptoms',
            field_required='housemates_with_flu_symptoms_count')
