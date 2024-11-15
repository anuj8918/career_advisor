# Generated by Django 4.2.3 on 2023-07-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0005_alter_assessmentscore_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='assessment_scores',
        ),
        migrations.AddField(
            model_name='assessmentscore',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='career.student'),
        ),
    ]
