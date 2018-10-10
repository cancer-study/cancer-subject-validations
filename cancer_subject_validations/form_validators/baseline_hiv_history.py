from edc_constants.constants import YES
from edc_form_validators import FormValidator

class BaseLineHivHistoryFormValidator(FormValidator):
    
    def clean(self):
        self.required_if(
            YES,
            field='has_cd4',
            field_required='cd4_result',
        )
        
        
        