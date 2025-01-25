from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Correo Electrónico Destinatario')
    subject = forms.CharField(label='Asunto', max_length=200)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)
    attachment = forms.FileField(label='Adjunto', required=False)

class SMSForm(forms.Form):
    phone_number = forms.CharField(label='Número de Teléfono', max_length=15)
    message = forms.CharField(label='Mensaje', widget=forms.Textarea, max_length=160)
