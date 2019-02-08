from django import forms
from edc_constants.constants import FEMALE, MALE
from edc_form_validators import FormValidator


class SubjectConsentFormValidation(FormValidator):

    def clean(self):
        super().clean()
        self.clean_identity_gender()

    def clean_identity_gender(self):
        cleaned_data = self.cleaned_data
        identity = cleaned_data.get('identity')
        gender = cleaned_data.get('gender')

        gender_dict = {'1': MALE,
                       '2': FEMALE}

        if gender_dict.get(identity[4:5]) != gender:
            raise forms.ValidationError({
                'identity': 'Subject\'s identity must match gender. '
                f'Gender indicated as {gender}. Please correct.'})
