from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.db.models import Sum
from master.models import Master

from extenstion.utils import get_file_path


# Create your models here.


class Institute(models.Model):
    name = models.CharField(max_length=125)
    logo = models.ImageField(upload_to=get_file_path)
    description = RichTextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def course_count(self):
        course_number = self.courses.all().count()
        return course_number

    def student_count(self):
        students_number = self.students.all().count()
        return students_number

    def master_count(self):
        master_count = Master.objects.filter(courses__institute_id=self.id).count()
        return master_count

    def get_absolute_url(self):
        return reverse("institute:detail", args=[self.id])

    def total_earn(self):
        pass
        # earn = self.courses.course_all_income()
        # return earn
