# Generated by Django 4.0.3 on 2022-04-11 15:25

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import extenstion.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125, verbose_name='عنوان دوره')),
                ('logo', models.ImageField(upload_to=extenstion.utils.get_file_path, verbose_name='لوگوی دوره')),
                ('description', models.TextField(verbose_name='توضیحات دوره')),
                ('start_time', django_jalali.db.models.jDateField(verbose_name='تاریخ شروع')),
                ('finish_time', django_jalali.db.models.jDateField(verbose_name='تاریخ اتمام')),
                ('fee', models.PositiveIntegerField(verbose_name='شهریه')),
                ('status', models.CharField(choices=[('START', 'شروع نشده'), ('HOLD', 'در حال برگزاری'), ('FINISHED', 'اتمام یافته')], max_length=15, verbose_name='وضعیت دوره')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دوره')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت دوره')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='master.master', verbose_name='استاد')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
    ]
