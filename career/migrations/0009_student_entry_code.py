# Generated by Django 4.2.3 on 2023-07-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0008_subjectfield_subject_subject_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='entry_code',
            field=models.CharField(default='', max_length=7),
            preserve_default=False,
        ),
    ]