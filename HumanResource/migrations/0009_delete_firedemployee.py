# Generated by Django 3.1.5 on 2021-02-19 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0008_appointment_approvedappointment_employeeleave_firedemployee_pendingappointment_receiptionist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FiredEmployee',
        ),
    ]