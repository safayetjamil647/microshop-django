# Generated by Django 3.0.6 on 2020-05-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_auto_20200508_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='customer_paid',
            field=models.FloatField(default=0),
        ),
    ]
