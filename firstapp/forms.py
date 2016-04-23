from django import forms
from models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'edu' not in email:
            raise forms.ValidationError('please enter an .edu address')
        return email # also works if no return