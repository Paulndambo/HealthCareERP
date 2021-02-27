# Generated by Django 3.1.5 on 2021-02-24 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0006_auto_20210219_1645'),
        ('Procurement', '0001_initial'),
        ('Finance', '0006_drugsell'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_number', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('paid_on', models.DateTimeField()),
                ('payment_approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.departmentdirector')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procurement.purchase')),
            ],
        ),
    ]
