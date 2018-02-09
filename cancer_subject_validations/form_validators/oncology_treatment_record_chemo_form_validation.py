from edc_base.modelform_validators import FormValidator

from edc_constants.constants import YES


class OncologyTreatmentRecordChemoFormValidation(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='chemo_delays',
            field_required='why_delayed',
        )

        self.required_if(
            YES,
            field='chemo_reduced',
            field_required='why_reduced',
        )

        return self.cleaned_data
