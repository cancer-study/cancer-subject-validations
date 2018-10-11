from edc_constants.constants import YES
from edc_form_validators import FormValidator


class OTRRadiationFormValidation(FormValidator):

    def clean(self):
        required_fields = ['concomitant', 'amount_radiation']
        for required in required_fields:
            self.required_if(
                YES,
                field='radiation_details',
                field_required=required,)
