# Generated by Django 4.0.3 on 2022-04-16 19:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='description',
            field=ckeditor.fields.RichTextField(default='zxcvz'),
            preserve_default=False,
        ),
    ]
