from django.core.exceptions import ValidationError
from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class CurrentSymptomsFormValidation(FormValidator):

    def clean(self):
        required_fields = ['symptom_desc', 'patient_own_remedy',
                           'ra_advice']
        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    YES,
                    field='any_worry',
                    field_required=required,)

        if (self.cleaned_data.get('any_worry') == NO
                and self.cleaned_data.get('severity') != 'NOT_APPLICABLE'):
            message = {'severity': 'This field is Not Applicable'}
            self._errors.update(message)
            raise ValidationError(message)
        elif (self.cleaned_data.get('any_worry') == YES
                and self.cleaned_data.get('severity') == 'NOT_APPLICABLE'):
            message = {'severity': 'This field is Applicable'}
            self._errors.update(message)
            raise ValidationError(message)
