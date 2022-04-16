# Generated by Django 4.0.3 on 2022-04-16 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
        ('student', '0003_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='institute.institute'),
        ),
    ]
