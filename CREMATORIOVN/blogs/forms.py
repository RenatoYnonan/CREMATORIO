from cProfile import label
from django import forms
from .models import BlogPost
from tinymce.widgets import TinyMCE

class FormBlog(forms.ModelForm):
    class Meta:
        model =  BlogPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_a, field_b in self.fields.items():
            field_b.widget.attrs['class'] = 'form-control'

            if field_a == 'content_post':
                field_b.widget.attrs['id'] = 'content_post_blog'
                field_b.widget = TinyMCE(attrs={
                    'cols': 80,
                    'rows': 30,
                })
            if field_a == 'slug_post':
                field_b.widget =  forms.HiddenInput()