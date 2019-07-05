from edc_form_validators import FormValidator


class LabResultTbFormValidator(FormValidator):

    def clean(self):
        responses = ['Yes_(IPT)', 'Yes_(ATT)']
        self.required_if(
            *responses,
            field='tb_treatment',
            field_required='tb_treatment_start',
            required_msg='If participant is receiving any kind of treatment'
                         ', when did this treatment begin',
        )
