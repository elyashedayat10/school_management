from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    national_code = forms.CharField(label='کد ملی')
    first_name = forms.CharField(label='نام')
    last_name = forms.CharField(label='نام خانوادگی')
    phone_number = forms.CharField(label='شماره تماس')

    class Meta:
        model = Student
        fields = (
            'father_name',
            'father_phone_number',
            'mother_phone_numer',
            'home_number',
            'grade',
            'profile',
            'gender',
        )
        labels = {
            'father_name': 'نام پدر',
            'father_phone_number': 'شماره تلفن پدر',
            'mother_phone_numer': 'شماره تلفن مادر',
            'home_number': 'شماره منزل',
            'grade': 'پایه',
            'profile': 'تصویر پروفایل',
            'gender': 'جنسیت',
        }
