from edc_constants.constants import (YES, NEG, POS, NO)
from edc_form_validators import FormValidator


class SymptomsAndTestingFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='hiv_tested',
            field_required='hiv_test_result',
            required_msg='If subject has been tested for HIV, '
                         ' what was the test result?',
            not_required_msg='If subject has NEVER tested for HIV, '
                             'do not key any result details',)

        self.required_if(
            NEG,
            field='hiv_test_result',
            field_required='neg_date',
            required_msg='If most recent HIV test result is neg, '
                         'provide date of last negative result',
            inverse=POS,
            not_required_msg='Subject is POS, you cannot answer NEG date')

        self.required_if(
            POS,
            field='hiv_test_result',
            field_required='pos_date',
            required_msg='If most recent HIV test result is neg, '
                         'provied date of last positive result',
            inverse=NEG,
            not_required_msg='Subject is NEG, you cannot answer POS date')

        required_fields = ['arv_art_start_date', 'arv_art_now']
        required_msgs = {'arv_art_start_date': 'If patient has taken HAART,'
                                               ' provide the start date ',
                         'arv_art_now': 'If patient took HAART before, are'
                                        ' they taking HAART even now'}
        not_required_msgs = {'arv_art_start_date': 'If patient has NEVER '
                             'started HAART. You CANNOT provide a start date',
                             'arv_art_now': 'Patient has never taken HAART'}
        for required in required_fields:
            self.required_if(
                YES,
                field='arv_art_therapy',
                field_required=required,
                required_msg=required_msgs[required],
                not_required_msg=not_required_msgs[required])

        self.required_if(
            NO,
            field='arv_art_now',
            field_required='art_art_stop_date',
            required_msg='Patient has STOPPED taking HAART. '
                         'Please provide STOP DATE',
            not_required_msg='You CANNOT give a stop date because patient is '
                             'taking HAART NOW'
        )

        condition = self.cleaned_data.get('facility_first_seen') == '00-0-00'
        self.required_if_true(
            condition=condition,
            field_required='facility_first_seen_other',
            required_msg='if facility is 00-0-00, please provide the name '
                         'of the facility')
