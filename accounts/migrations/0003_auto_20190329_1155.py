# Generated by Django 2.1.2 on 2019-03-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190329_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name': 'Sale'},
        ),
    ]
