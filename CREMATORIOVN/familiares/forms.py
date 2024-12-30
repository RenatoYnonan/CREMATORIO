from django import forms
from .models import *

class FamiliaresForms(forms.ModelForm):
    class Meta:
        model = ModelsFamiliar 
        fields = '__all__'   


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estado'].widget =  forms.HiddenInput()

        placeholders = {
            'name': 'Nombre Completo',
            'lastname': 'Apellido',
            'telephone': 'N° de celular',
            'email': 'Ingresa tu correo electrónico',
            'city': 'Ingresa la ciudad',
            'number_document': 'Número de documento',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
            
    