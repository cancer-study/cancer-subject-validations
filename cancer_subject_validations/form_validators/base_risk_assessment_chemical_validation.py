from edc_constants.constants import YES
from edc_form_validators import FormValidator


class BaseRiskAssessmentChemicalValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='abestos_no_protection',
            field_required='how_long',
            )

        self.required_if(
            YES,
            field='other_chemicals',
            field_required='how_long',
            )

        self.required_if(
            YES,
            field='arsenic_smelting',
            field_required='how_long',
            )
