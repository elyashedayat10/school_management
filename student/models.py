from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse
from extenstion.utils import CustomCharField, get_file_path
from institute.models import Institute

user = get_user_model()


# Create your models here.
class Student(models.Model):
    GENDER = (
        ("پسر", "پسر"),
        ("دختر", "دخنر"),
    )
    user = models.OneToOneField(
        user,
        on_delete=models.CASCADE,
        limit_choices_to=user.objects.filter(is_student=True),
    )
    father_name = models.CharField(
        max_length=125,
    )
    father_phone_number = CustomCharField()
    mother_phone_numer = CustomCharField()
    home_number = models.CharField(
        max_length=10,
    )
    grade = models.ManyToManyField(
        "Grade",
    )
    profile = models.ImageField(
        upload_to=get_file_path,
    )
    gender = models.CharField(
        max_length=4,
        choices=GENDER,
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name='students',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.user}-{self.institute}'

    def get_absolute_url(self):
        return reverse('Student:detail', args=[self.id])



class Grade(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Grade, self).save(*args, **kwargs)


def create_student(sender, **kwargs):
    if kwargs["created"]:
        if kwargs["instance"].is_student:
            p1 = Student(user=kwargs["instance"])
            p1.save()


post_save.connect(sender=user, receiver=create_student)
