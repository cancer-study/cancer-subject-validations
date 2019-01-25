from django.core.exceptions import ValidationError
from edc_form_validators import FormValidator
from edc_constants.choices import YES


class BaseRiskAssessmentFemaleValidation(FormValidator):

    def clean(self):
        condition = self.cleaned_data['children'] == 0
        if condition:
            if self.cleaned_data['years_breastfed'] and self.cleaned_data['years_breastfed'] == YES:
                msg = {'years_breastfed': 'You specified that you never had a child'
                       ' before, this field is not required'}
                self._errors.update(msg)
                raise ValidationError(msg)
