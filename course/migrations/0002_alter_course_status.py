# Generated by Django 4.0.3 on 2022-04-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('START', 'شروع نشده'), ('HOLD', 'در حال برگزاری'), ('FINISHED', 'اتمام یافته')], default='شروع نشده', max_length=15, verbose_name='وضعیت دوره'),
        ),
    ]
