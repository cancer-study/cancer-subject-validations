from edc_constants.constants import YES
from edc_form_validators import FormValidator


class OTRChemoFormValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='chemo_delayed',
            field_required='why_delayed',)

        self.required_if(
            YES,
            field='chemo_reduced',
            field_required='why_reduced',
        )
