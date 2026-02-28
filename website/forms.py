import re
from django import forms
from .models import ContactMessage, QuoteRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'mobile', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Your mobile number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'mobile': 'Mobile No.',
            'message': 'Leave us a few words',
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not re.match(r'^\+?[\d\s\-]{7,20}$', mobile):
            raise forms.ValidationError('Please enter a valid mobile number.')
        return mobile


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'mobile', 'service_type', 'description', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Your mobile number'}),
            'service_type': forms.Select(),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your requirement in detail (dimensions, material, location, etc.)'
            }),
            'budget': forms.TextInput(attrs={'placeholder': 'e.g. ₹50,000 – ₹1,00,000'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'mobile': 'Mobile No.',
            'service_type': 'Service Required',
            'description': 'Project Description',
            'budget': 'Approximate Budget (optional)',
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '').strip()
        if not re.match(r'^\+?[\d\s\-]{7,20}$', mobile):
            raise forms.ValidationError('Please enter a valid mobile number.')
        return mobile
