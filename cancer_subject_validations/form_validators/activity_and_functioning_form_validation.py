from django.core.exceptions import ValidationError
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

        housemates_with_symptoms = self.cleaned_data.get(
            'housemates_with_flu_symptoms_count')

        housemates_count = self.cleaned_data.get('housemates_count')

        if housemates_with_symptoms:
            if (housemates_with_symptoms > housemates_count):
                message = {
                    'housemates_with_flu_symptoms_count':
                    'The number of housemates developing cold or flu like '
                    f'symptoms {housemates_with_symptoms} can not be greater '
                    'than the number of people that live in your household '
                    f'{housemates_count}.'
                }
                self._errors.update(message)
                raise ValidationError(message)
