from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email
