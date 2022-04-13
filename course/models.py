from ckeditor.fields import RichTextField
from django.db import models
from django_jalali.db import models as jmodels

from extenstion.utils import get_file_path
from master.models import Master
from student.models import Grade

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
        verbose_name="عنوان دوره",
    )
    logo = models.ImageField(
        upload_to=get_file_path,
        verbose_name="لوگوی دوره",
    )
    # description = RichTextField()
    description = models.TextField(
        verbose_name="توضیحات دوره",
    )
    start_time = jmodels.jDateField(
        verbose_name="تاریخ شروع",
    )
    finish_time = jmodels.jDateField(
        verbose_name="تاریخ اتمام",
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="استاد",
    )
    fee = models.PositiveIntegerField(
        verbose_name="شهریه",
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        verbose_name="وضعیت دوره",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد دوره",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ آپدیت دوره",
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    # participation=models.ManyToManyField()

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return f"{self.master.last_name}-{self.title}"

    def get_absolute_url(self):
        pass
