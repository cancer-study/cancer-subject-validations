from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class SubjectConsentFormValidation(FormValidator):

    def clean(self):

        field_required_list = ['unconcious',
                               'abnormal_mind']
        for fields in field_required_list:
            self.required_if(
                YES,
                field=fields,
                field_required='guadian_name'
            )

        return self.cleaned_data
