from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class BaselineHivHistoryCd4ResultFormValidation(FormValidator):

    def clean(self):

        field_required_list = ['cd4_result', 'cd4_drawn_date',
                               ]
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='has_cd4',
                field_required=required
            )

            field_required_list = ['nadir_cd4', 'years_smoked',
                                   ]
        for required in field_required_list:
            self.not_required_if(
                YES,
                field='has_prior_cd4',
                field_required=required
            )

        return self.cleaned_data
