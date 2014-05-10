from django import forms
from django.utils.translation import ugettext_lazy as _

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

    first_name_ja = forms.CharField(
        label=_("First Name (Japanese)"),
        required=False,
        max_length=50,
        help_text=_("Please enter your first  name in Japanese. "
                    "Non-Japanese can leave this blank.")
    )
    last_name_ja = forms.CharField(
        label=_("Last Name (Japanese)"),
        required=False,
        max_length=50,
        help_text=_("Please enter your last name in Japanese. "
                    "Non-Japanese can leave this blank.")
    )

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

        self.fields['email'].label = _("Email")
        self.fields['email_confirm'].label = _("Confirm Email")

        self.fields['first_name'].label = _("First Name")
        self.fields['first_name'].help_text = _("Please enter your first name.")
        self.fields['last_name'].label = _("Last Name")
        self.fields['last_name'].help_text = _("Please enter your last name.")
