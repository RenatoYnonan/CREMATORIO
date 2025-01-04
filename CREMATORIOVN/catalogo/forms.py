from django.forms import ModelForm
from .models import *

class FormsProduct(ModelForm):
    class Meta:
        model = ModelsProduct
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

