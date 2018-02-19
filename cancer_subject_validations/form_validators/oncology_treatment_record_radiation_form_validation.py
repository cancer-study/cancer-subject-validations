from edc_form_validators import FormValidator

from edc_constants.constants import YES


class OncologyTreatmentRecordRadiationFormValidation(FormValidator):

    def clean(self):
        field_required_list = ['concomitant',
                               'amount_radiation']
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='radiation_details',
                field_required=required
            )

        return self.cleaned_data
