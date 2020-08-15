from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthWithRememberingSession(AuthenticationForm):
    remember_me = forms.BooleanField(initial=True,
                                     label='Remember me',
                                     required=False)

