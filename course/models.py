from ckeditor.fields import RichTextField
from django.db import models
from django_jalali.db import models as jmodels

from extenstion.utils import get_file_path
from master.models import Master

# Create your models here.

class Course(models.Model):
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
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    # participation=models.ManyToManyField()

    class Meta:
        pass

    def __str__(self):
        return f'{self.master.last_name}-{self.title}'

    def get_absolute_url(self):
        pass
