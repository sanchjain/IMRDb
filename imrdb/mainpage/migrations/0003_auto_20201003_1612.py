# Generated by Django 3.1 on 2020-10-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20201003_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_name',
            new_name='name',
        ),
    ]
