# Generated by Django 2.1.2 on 2019-03-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190329_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]