from django import forms
from .models import ProveedoresModels

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = ProveedoresModels
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'
