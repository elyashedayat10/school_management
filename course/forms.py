from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "title",
            "logo",
            "description",
            "start_time",
            "finish_time",
            "master",
            "fee",
        )
        labels = {
            "title": "عنوان",
            "logo": "تصویر",
            "description": "توضیحات دوره",
            "start_time": "شروع دوره",
            "finish_time": "پایان دوره",
            "master": "استاد",
            "fee": "شهریه دوره",
        }


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "title",
            "logo",
            "description",
            "start_time",
            "finish_time",
            "master",
            "fee",
            "status",
        )
        labels = {
            "title": "عنوان",
            "logo": "تصویر",
            "description": "توضیحات دوره",
            "start_time": "شروع دوره",
            "finish_time": "پایان دوره",
            "master": "استاد",
            "fee": "شهریه دوره",
            "status": "وضعیت",
        }
