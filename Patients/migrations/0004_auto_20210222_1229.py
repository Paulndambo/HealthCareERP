# Generated by Django 3.1.5 on 2021-02-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_auto_20210222_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientvisit',
            old_name='patient',
            new_name='name',
        ),
    ]