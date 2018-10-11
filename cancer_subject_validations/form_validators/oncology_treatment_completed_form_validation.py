from edc_constants.constants import YES
from edc_form_validators import FormValidator


class OncologyTreatmentCompletedFormValidator(FormValidator):

    def clean(self):

        fields = ['patient_had_chemo', 'patient_had_radiation',
                  'patient_had_surgery']
        for field in fields:
            self.required_if(
                YES,
                field=field,
                field_required='treatment_detail',
                required_msg='Treatment is planned. Please provide details'
                             ' of the treatment')
