from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify

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
        related_name="students",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user}-{self.institute}"

    def get_absolute_url(self):
        return reverse("Student:detail", args=[self.pk])

    def total_pay(self):
        total_paying_estimate = self.course_set.aggregate(Sum("fee"))["fee__sum"]
        return total_paying_estimate

    def get_course_count(self):
        course_count = self.course_set.all().only("id").count()
        return course_count


class installment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="installment",
    )
    paid = models.BooleanField(
        default=False,
    )
    amount = models.IntegerField()


class BaseEducation(models.Model):
    title = models.CharField(
        max_length=125,
    )
    created = models.DateField(
        auto_now_add=True,
    )
    # institute = models.ManyToManyField(
    #     Institute,
    #     related_name="%(app_label)s_%(class)s_related",
    #     related_query_name='%(app_label)s_%(class)ss'
    # )

    class Meta:
        abstract = True


class Grade(BaseEducation):
    major = models.ManyToManyField(
        "Major",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Student:grade_detail", args=[self.id])

    def grade_student_count(self):
        student_count = self.student_set.all().values("id").count()
        return student_count

    def get_course_count(self):
        pass
        # course_count = self.institute.courses.filter(grade_id=self.id)
        # return course_count


class Major(BaseEducation):
    def __str__(self):
        return self.title


def create_student(sender, **kwargs):
    if kwargs["created"]:
        if kwargs["instance"].is_student:
            p1 = Student(user=kwargs["instance"])
            p1.save()


post_save.connect(sender=user, receiver=create_student)
