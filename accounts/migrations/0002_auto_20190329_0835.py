# Generated by Django 2.1.2 on 2019-03-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='kg_of_tea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unit_cost',
            field=models.IntegerField(),
        ),
    ]
