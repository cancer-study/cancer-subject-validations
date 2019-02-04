from edc_constants.constants import YES, NO
from edc_form_validators import FormValidator


class OncologyTreatmentPlanFormValidator(FormValidator):

    def clean(self):
        required_fields = ['chemotherapy', 'radiation_plan',
                           'surgical_plan']
        for required in required_fields:
            self.required_if(
                YES,
                field='treatment_plan',
                field_required=required,)

        condition = (self.cleaned_data.get('chemotherapy') != YES or
                     self.cleaned_data.get('radiation_plan') != YES or
                     self.cleaned_data.get('surgical_plan') != YES)
        self.required_if_true(
            condition=condition,
            field_required='chemotherapy',
            required_msg='Chemotherapy ')

        self.required_if(
            YES,
            field='chemotherapy',
            field_required='chemo_intent',
            required_msg='if chemotherapy is planned, what is the '
                         'intent of giving it?',
            not_required_msg='NO chemo intent should be provided. '
                             'chemotherapy is not planned',
            inverse=True,)

        self.required_if(
            YES,
            field='surgical_plan',
            field_required='planned_operation',
            required_msg='If surgery is planned, describe the '
                         'planned operation',
            not_required_msg='NO surgery planned. Do not describe planned '
                             'operation',
            inverse=True,)
