from django.core.validators import ValidationError
from django.db import models
from django.urls import reverse
from extenstion.utils import get_file_path


def validate_national_code(value):
    if value.isnumeric() in value | len(value) == 10:
        return value
    else:
        raise ValidationError("This field accepts int only and character must be 10")


# Create your models here.
class Master(models.Model):
    first_name = models.CharField(
        max_length=125,
    )
    last_name = models.CharField(
        max_length=125,
    )
    national_code = models.CharField(
        max_length=125,
        validators=[validate_national_code]
    )
    profile_image = models.ImageField(
        upload_to=get_file_path,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        pass

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

    def get_absolute_url(self):
        return reverse('Master:master_detail', args=[self.id])

    def master_course_count(self):
        course_count = self.courses.count()
        return course_count
