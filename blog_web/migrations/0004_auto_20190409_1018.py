# Generated by Django 2.1.2 on 2019-04-09 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_web', '0003_auto_20190402_0550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
    ]
