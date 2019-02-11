
from django.core.exceptions import ValidationError
from edc_form_validators import FormValidator


class LabResultsHeightWeightValidator(FormValidator):

    def clean(self):
        self.require_together(
            field='height',
            field_required='weight',
            required_msg='Please enter a numeric value for height')

        self.height = self.cleaned_data['height']
        self.weight = self.cleaned_data['weight']

        if not self.height:
            raise ValidationError('Please enter a numeric value for height')

        if not self.weight:
            raise ValidationError('Please enter a numeric value for weight')

