# Generated by Django 3.1.5 on 2021-02-24 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0019_auto_20210225_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Pharmacy', 'Pharmacy'), ('Finance', 'Finance'), ('Laboratory', 'Laboratory'), ('Procurement', 'Procurement')], max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='graduation_year',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hair_color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='height',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='highest_education_level',
            field=models.CharField(choices=[("Bachelor's Degree", "Bachelor's Degree"), ('Masters Degree', 'Masters Degree'), ('PhD', 'PhD')], max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_university_attended',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_photo',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='schools_attended',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='skin_color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='specialization',
            field=models.CharField(max_length=500),
        ),
    ]
