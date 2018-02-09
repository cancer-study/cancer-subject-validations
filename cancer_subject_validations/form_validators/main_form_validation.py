from edc_base.modelform_validators import FormValidator
from edc_constants.constants import (YES, NO, NEG)


class MainFormValidator (FormValidator):

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

            field_required_list = ['chemotherapy', 'radiation_plan'
                                   'surgical_plan']
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='treatment_plan',
                field_required=required
            )

            self.required_if(
                YES,
                field='hiv_tested',
                field_required='hiv_tested_result')

        field_list = ['hiv_tested', 'hiv_test_result', 'arv_art_therapy'
                      'arv_art_now'
                      ]
        field_required_list = ['hiv_test_result', 'neg_date', 'pos_date',
                               'arv_art_start_date', 'arv_art_now',
                               'arv_stop_date']

        for field, field_required in zip(field_list, field_required_list):
            self.required_if(
                'POS', 'NEG', YES, NO,
                field=field,
                field_required=field_required)

#             field_required_list = ['arv_art_start_date',
#                                    'arv_art_stop_date'
#                                    'arv_art_now']
#         for required in field_required_list:
#             self.not_required_if(
#                 YES, NO,
#                 field='arv_art_therapy',
#                 field_required=required
#             )

            self.required_if(
                YES,
                field='patient_had_chemo',
                field_required='treatment_detail')

        field_list = ['patient_had_chemo', 'patient_had_surgery'
                      'patient_had_radiation'
                      ]
        field_required_list = ['treatment_detail']

        for field, field_required in zip(field_list, field_required_list):
            self.required_if(
                YES,
                field=field,
                field_required=field_required)

            field_required_list = ['symptom_desc',
                                   'patient_own_remedy'
                                   'severity']
        for required in field_required_list:
            self.not_required_if(
                YES, NO,
                field='any_worry',
                field_required=required
            )
        return self.cleaned_data
