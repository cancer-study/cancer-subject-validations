from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class MainCurrentSymptomsFormValidation (FormValidator):

    def clean(self):

        field_required_list = ['symptom_desc',
                               'patient_own_remedy',
                               'severity']
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='any_worry',
                field_required=required
            )
        return self.cleaned_data
