from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class MainCancerDiagnosisFormValidaton (FormValidator):

    def clean(self):

        field_required_list = ['cancer_category', 'date_diagnosed',
                               'diagnosis_basis', 'diagnosis_word',
                               'cancer_site'
                               ]
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='diagnosis',
                field_required=required
            )
