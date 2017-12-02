from django import forms
from .models import Post
from django.core import validators

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'image',
                  'text',
                  'contact',
                  'lost_or_found',
                  'zone',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a short Description'}),
            'contact': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please write your contact Information here'}),
        }

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder': 'Enter Your Name',
        }
    ))

    Email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 'placeholder':'Enter Your Email',
        }
    ))

    Message = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control', 'placeholder': 'Enter Your Message',
        }
    ))
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty", validators=[validators.MaxLengthValidator(0)])