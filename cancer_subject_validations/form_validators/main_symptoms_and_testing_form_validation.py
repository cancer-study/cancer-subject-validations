from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class MainSymptomsAndTestingFormValidaton (FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='hiv_tested',
            field_required='hiv_test_result',
        )

        self.not_required_if(
            'NEG',
            field='hiv_test_result',
            field_required='neg_date',
        )

        self.not_required_if(
            'NEG',
            field='hiv_test_result',
            field_required='pos_date',
        )

        self.required_if(
            'POS',
            field='hiv_test_result',
            field_required='pos_date',
        )

        self.not_required_if(
            'POS',
            field='hiv_test_result',
            field_required='neg_date',
        )

        field_required_list = ['hiv_test_result',
                               'pos_date'
                               ]
        for required in field_required_list:
            self.not_required_if(
                NO,
                field='hiv_tested',
                field_required=required
            )

            self.required_if(
                YES,
                field='arv_art_therapy',
                field_required='arv_art_start_date',
            )

            self.required_if(
                YES,
                field='arv_art_therapy',
                field_required='arv_art_now',
            )

            self.not_required_if(
                NO,
                field='arv_art_therapy',
                field_required='arv_art_start_date',
            )

            self.not_required_if(
                NO,
                field='arv_art_now',
                field_required='arv_art_stop_date',
            )

            self.required_if(
                NO,
                field='arv_art_now',
                field_required='arv_art_stop_date',
            )

            self.not_required_if(
                YES,
                field='arv_art_now',
                field_required='arv_art_stop_date',
            )

        return self.cleaned_data
