from django.conf import settings

if settings.APP_NAME == 'cancer_subject_validations':
    from .tests import models
