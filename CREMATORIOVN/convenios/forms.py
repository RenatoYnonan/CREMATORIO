from django import forms
from .models import *

class FuneriasForm(forms.ModelForm):
    class Meta:
        model = ModelsFunerarias
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        placeholder = {
            'nombre_funeraria' : 'Nombre de la Funeraria',
            'ciudad': 'Nombre de la ciudad',
            'redes_sociales':  'Ingresa la Url de la red social',
        }

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'
            
            if field_a in  placeholder:
                field_b.widget.attrs['placeholder'] = placeholder[field_a]


class InstitucionesForm(forms.ModelForm):
    class Meta:
        model = ModelsInstitucion
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'
            