from edc_form_validators import FormValidator


class BaseRiskAssessmentFemaleValidation(FormValidator):

    def clean(self):
        condition = self.cleaned_data['children'] > 0
        self.required_if_true(
            condition,
            field_required='years_breastfed',
            not_required_msg='You specified that you never had a child'
            ' before, this field is not required'
        )
