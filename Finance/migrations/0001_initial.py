# Generated by Django 3.1.5 on 2021-02-22 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0006_auto_20210219_1645'),
        ('HumanResource', '0012_auto_20210219_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=20)),
                ('paid_on', models.DateTimeField()),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.departmentdirector')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
            options={
                'verbose_name_plural': 'Salaries Payments',
            },
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
        ),
    ]
