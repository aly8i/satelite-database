# Generated by Django 4.0.5 on 2022-07-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_account_month_alter_account_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phonenumber',
            field=models.CharField(max_length=12),
        ),
    ]
