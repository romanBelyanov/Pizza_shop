from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'from-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'from-input'}))
