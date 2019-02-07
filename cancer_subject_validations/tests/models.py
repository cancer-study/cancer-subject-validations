from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin


class SubjectConsent(UpdatesOrCreatesRegistrationModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    gender = models.CharField(max_length=25)


class SubjectVisit(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    visit_code = models.CharField(max_length=25)

    visit_code_sequence = models.IntegerField(default=0)

    report_datetime = models.DateTimeField(
        default=get_utcnow())
