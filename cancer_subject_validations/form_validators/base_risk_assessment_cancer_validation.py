from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from edc_constants.constants import YES, MALE
from edc_form_validators import FormValidator
from edc_form_validators.base_form_validator import NOT_REQUIRED_ERROR


class BaseRiskAssessementCancerFormValidator(FormValidator):

    consent_cls = 'cancer_subject.subjectconsent'

    @property
    def consent_model(self):
        return django_apps.get_model(self.consent_cls)

    def clean(self):
        self.required_if(
            YES,
            field='family_cancer',
            field_required='family_cancer_type',
        )

        self.required_if(
            YES,
            field='had_previous_cancer',
            field_required='previous_cancer'
        )
        self.verify_cancer_type()

    def verify_cancer_type(self):
        try:
            gender = self.consent_model.objects.get(
                subject_identifier=self.cleaned_data.get(
                    'subject_visit').subject_identifier).gender
        except self.consent_model.DoesNotExist:
            raise ValidationError(
                'Please complete consent before proceeding.')
        else:
            if gender == MALE:
                if(self.cleaned_data.get(
                    'family_cancer_type') == 'cervical_cancer'
                        or self.cleaned_data.get(
                            'previous_cancer') == 'cervical_cancer'):
                    message = {'family_cancer_type': 'Participant is male, cervical cancer is not a '
                               ' valid choice.'}
                    self._errors.update(message)
                    self._error_codes.append(NOT_REQUIRED_ERROR)
                    raise ValidationError(message, code=NOT_REQUIRED_ERROR)
