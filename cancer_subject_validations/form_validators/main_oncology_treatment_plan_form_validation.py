from edc_form_validators import FormValidator
from edc_constants.constants import YES


class MainOncologyTreatmentPlanFormValidaton (FormValidator):

    def clean(self):

        field_required_list = ['chemotherapy', 'radiation_plan',
                               'surgical_plan'
                               ]
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='treatment_plan',
                field_required=required
            )
