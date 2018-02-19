from edc_form_validators import FormValidator

from ..constants.lab_result_tb_form_constants import (
    YES_ISONIAZID_PREVENTATIVE_THERAPY, YES_COMBINATION_ANTI_TB)


class LabResultTbFormValidation(FormValidator):

    def clean(self):

        self.required_if(
            YES_ISONIAZID_PREVENTATIVE_THERAPY,
            field='tb_treatment',
            field_required='tb_treatment_start',
        )

        self.required_if(
            YES_COMBINATION_ANTI_TB,
            field='tb_treatment',
            field_required='tb_treatment_start',
        )

        return self.cleaned_data
