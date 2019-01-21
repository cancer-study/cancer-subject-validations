from django.core.exceptions import ValidationError
from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class CancerDiagnosisFormValidator(FormValidator):

    def clean(self):
        required_fields = ['cancer_category', 'date_diagnosed',
                           'diagnosis_basis']

        for required in required_fields:
            if required in self.cleaned_data:
                self.required_if(
                    YES,
                    field='diagnosis',
                    field_required=required)

        required_fields = ['diagnosis_word', 'cancer_site']
        condition = self.cleaned_data.get('date_diagnosed') != None
        for required in required_fields:
            self.required_if_true(
                condition=condition,
                field_required=required)

        if self.cleaned_data.get('diagnosis') == NO:
            message = {'diagnosis':
                       'AT enrollment you mentioned that a cancer diagnosis '
                       'was documented, so answer to whether a cancer diagnosis '
                       'has been made should be YES. please correct!'}
            self._errors.update(message)
            raise ValidationError(message)
