# Generated by Django 3.1.5 on 2021-02-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0015_employee_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]