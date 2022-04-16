from django.db import models
from extenstion.utils import get_file_path


# Create your models here.


class Institute(models.Model):
    name = models.CharField(max_length=125)
    logo = models.ImageField(upload_to=get_file_path)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    def student_count(self):
        students_number = self.students.all().count()
        return students_number

    def __str__(self):
        return self.name
