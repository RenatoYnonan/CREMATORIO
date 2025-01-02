from django import forms
from .models import *

class FormSocial(forms.ModelForm):
    class Meta:
        model = SocialNetworks
        fields = '__all__'

    def __init__(self, *args, **kargs):

        super().__init__(*args, **kargs)

        if 'url' in self.fields:
            self.fields['url'].widget.attrs['placeholder'] = 'Ingrese la url'

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'


class FormCompany(forms.ModelForm):
    class Meta:
        model = CompanyConf
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


        placeholder_company = {
            'name_company' : 'Ingrese el nombre de la empresa',
            'slogan_company': 'Ingrese el slogan de la empresa',
            'addres_company': 'Ingrese la dirección de su empresa ',
            'gmail_company':'Ingresa el gmail de la empresa',
            'phone_company': 'Ingrese el número de Teléfono'
        }

        for field_a, field_b  in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

            if field_a in placeholder_company:
                field_b.widget.attrs['placeholder'] = placeholder_company[field_a]

