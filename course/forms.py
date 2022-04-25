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
            "institute",
            "grade",
        )
        labels = {
            "title": "عنوان",
            "logo": "تصویر",
            "description": "توضیحات دوره",
            "start_time": "شروع دوره",
            "finish_time": "پایان دوره",
            "master": "استاد",
            "fee": "شهریه دوره",
            "institute": "آموزشگاه",
            "grade": "پایه",
        }


class InstituteCourseForm(CourseCreateForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields.pop("institute")


class CourseUpdateForm(CourseCreateForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields.pop("institute")
        self.fields.append("status")
