from django import forms
from .models import *


class FallecidosForms(forms.ModelForm):
    class Meta:
        model = Fallecido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

            if field_a == 'fecha_nacimiento' or field_a == 'fecha_fallecido':
                field_b.widget = forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })


class CondolenciaForms(forms.ModelForm):
    class Meta:
        model =  Condolencias
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields['fecha_creacion'].widget = forms.HiddenInput()


        for a, b in self.fields.items():
            b.widget.attrs['class'] = 'form-control'

        if 'nombre_fallecido' in self.fields:
            del self.fields['nombre_fallecido']
            

    
    
