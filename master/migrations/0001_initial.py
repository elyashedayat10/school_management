# Generated by Django 4.0.3 on 2022-04-16 21:57

import django.core.validators
from django.db import migrations, models

import extenstion.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=125, verbose_name="نام")),
                (
                    "last_name",
                    models.CharField(max_length=125, verbose_name="نام خانوادگی"),
                ),
                (
                    "national_code",
                    models.CharField(
                        max_length=125,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]{10}$", "same as pattern"
                            )
                        ],
                        verbose_name="کد ملی",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        upload_to=extenstion.utils.get_file_path,
                        verbose_name="تصویر پزوفایل",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="تاریخ به روز رسانی"
                    ),
                ),
            ],
            options={
                "verbose_name": "استاد",
                "verbose_name_plural": "اساتید",
            },
        ),
    ]
