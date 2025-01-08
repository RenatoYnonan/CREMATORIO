from django import forms
from .models import *

class FormsProduct(forms.ModelForm):
    class Meta:
        model = ModelsProduct
        fields = '__all__'
        # widgets = {
        #     'planes' :  forms.RadioSelect(attrs={'class': 'd'})
        # }
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)



        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

            if field_a == 'planes':
                field_b.widget.attrs['class'] = 'custom-select'


class FormPlanes(forms.ModelForm):
    class Meta:
        model = ModelsPlanes
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        


        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

