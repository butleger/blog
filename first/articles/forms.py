from django import forms


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=20, help_text='your fucking title')
    text = forms.CharField(widget=forms.Textarea, label='your article')


class AddCommentForm(forms.Form):
    author = forms.CharField(max_length=20, required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment_input',
                                                        'rows' : 3}))

class CreateUserForm(forms.Form):
    password1 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'pass_input'}),
                                label='Confirm')
    password2 = forms.CharField(max_length=20,
                                widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                  'class': 'pass_input'}),
                                label='Confirm')