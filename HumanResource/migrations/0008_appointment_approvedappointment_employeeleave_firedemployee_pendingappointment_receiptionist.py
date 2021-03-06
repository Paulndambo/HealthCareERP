# Generated by Django 3.1.5 on 2021-02-19 13:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0007_auto_20210219_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_by', models.CharField(max_length=200)),
                ('appointment_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('appointment_request_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Receiptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Day', 'Day'), ('Night', 'Night')], max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
        ),
        migrations.CreateModel(
            name='PendingAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why_not_approved', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='FiredEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firing_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('firing_reason', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
            options={
                'verbose_name': 'Fired Employee',
                'verbose_name_plural': 'Fired Employees',
            },
        ),
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_request_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('leave_reason', models.TextField()),
                ('days_to_be_off', models.IntegerField(verbose_name='how many days do you want to off')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
            options={
                'verbose_name': 'Employees Leave Request',
                'verbose_name_plural': 'Employees Leave Requests',
            },
        ),
        migrations.CreateModel(
            name='ApprovedAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.appointment')),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.receiptionist')),
            ],
        ),
    ]
