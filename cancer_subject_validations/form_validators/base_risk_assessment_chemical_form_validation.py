from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessmentChemicalValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='asbestos',
            field_required='asbestos_no_protection',
        )

        self.required_if(
            YES,
            field='chemicals',
            field_required='chemicals_time',
        )

        self.required_if(
            YES,
            field='arsenic_smelting',
            field_required='total_time_no_protection',
        )
