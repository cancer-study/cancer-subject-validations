from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from edc_constants.constants import YES
from edc_form_validators import FormValidator


class OncologyTreatmentCompletedFormValidator(FormValidator):

    oncology_treatment_plan_model = 'cancer_subject.oncologytreatmentplan'

    @property
    def oncology_treatment_plan_cls(self):
        return django_apps.get_model(self.oncology_treatment_plan_model)

    def clean(self):

        fields = ['patient_had_chemo', 'patient_had_radiation',
                  'patient_had_surgery']
        for field in fields:
            self.required_if(
                YES,
                field=field,
                field_required='treatment_detail',
                required_msg='Treatment is planned. Please provide details'
                             ' of the treatment')
        self.validate_surgery_plan()

    def validate_surgery_plan(self):

        oncology_treatment_plan = self.oncology_treatment_plan_cls.objects.filter(
            subject_identifier=self.cleaned_data.get('subject_visit'
                                                     ).appointment.subject_identifier
            ).order_by('created').first()

        if oncology_treatment_plan and oncology_treatment_plan.surgical_plan != YES:
            message = {'patient_had_surgery':
                       'According to Oncology Treatment Plan @ 1000 visit, '
                       'Patient was supposed to have surgery, this field must be No.'}
            self._errors.update(message)
            raise ValidationError(message)
