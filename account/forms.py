from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

user = get_user_model()


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = (
            'national_code',
            'phone_number',
            'first_name',
            'last_name',
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\">this form</a>."
    )

    class Meta:
        model = user
        fields = (
            'national_code',
            'phone_number',
            'first_name',
            'last_name',
            'password',
            'last_login',
        )


class LoginForm(forms.Form):
    national_code = forms.CharField(
        max_length=10,
        label='کذ ملی',
        widget=forms.TextInput(attrs={'class': 'form-control'},
                               ))
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'},
                                   ))


class AdminCreateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'national_code',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )
        labels = {
            'national_code': 'کد ملی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماه تماس',
            'password': 'رمز عبور'
        }


class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'national_code',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )
        labels = {
            'national_code': 'کد ملی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماه تماس',
            'password': 'رمز عبور'
        }
