
from django.core.exceptions import ValidationError
from edc_form_validators import FormValidator


class LabResultsHeightWeightValidator(FormValidator):

    def clean(self):
        if not self.cleaned_data.get('weight'):
            raise ValidationError('Please enter a numeric value for weight')

        if not self.cleaned_data.get('height'):
            raise ValidationError('Please enter a numeric value for height')
