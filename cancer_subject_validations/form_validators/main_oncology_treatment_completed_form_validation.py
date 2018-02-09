from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class MainOncologyTreatmentCompletedFormValidation (FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='patient_had_chemo',
            field_required='treatment_detail',
        )

        self.required_if(
            YES,
            field='patient_had_radiation',
            field_required='treatment_detail',
        )

        self.required_if(
            YES,
            field='patient_had_surgery',
            field_required='treatment_detail',
        )

        return self.cleaned_data
