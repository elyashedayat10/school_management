import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django_jalali.db import models as jmodels


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/' + instance.model, filename)


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# Create your models here.
class Master(TimeStamp):
    first_name = models.CharField(
        max_length=125,
    )
    last_name = models.CharField(
        max_length=125,
    )
    national_code = models.CharField(
        max_length=125,
    )
    profile_image = models.ImageField(
        upload_to=get_file_path,
        blank=True,
    )

    class Meta:
        pass

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

    def get_absolute_url(self):
        pass

    def master_course_count(self):
        course_count = self.courses.count()
        return course_count


class Course(TimeStamp):
    STATUS = (
        ("START", "شروع نشده"),
        ("HOLD", "در حال برگزاری"),
        ("FINISHED", "اتمام یافته"),
    )
    objects = jmodels.jManager()
    title = models.CharField(
        max_length=125,
    )
    logo = models.ImageField(
        upload_to=get_file_path,
    )
    description = RichTextField()
    start_time = jmodels.jDateField()
    finish_time = jmodels.jDateField()
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    fee = models.PositiveIntegerField()
    status = models.CharField(
        max_length=15,
        choices=STATUS,
    )

    # participation=models.ManyToManyField()

    class Meta:
        pass

    def __str__(self):
        return f'{self.master.last_name}-{self.title}'

    def get_absolute_url(self):
        pass
