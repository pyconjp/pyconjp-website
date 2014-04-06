from django import forms

from symposion.forms import SignupForm

from .models import Profile


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ['phone']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        
        self.fields.keyOrder = [
            "first_name",
            "first_name_ja",
            "last_name",
            "last_name_ja",
        ]


class SignupForm(SignupForm):

    first_name_ja = forms.CharField(required=False)
    last_name_ja = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            "email",
            "email_confirm",
            "first_name",
            "first_name_ja",
            "last_name",
            "last_name_ja",
            "password",
            "password_confirm"
        ]
