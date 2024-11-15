# Generated by Django 4.2.3 on 2023-08-02 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0011_assessmentscore_total_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('subject_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='career.subjectfield')),
            ],
        ),
    ]