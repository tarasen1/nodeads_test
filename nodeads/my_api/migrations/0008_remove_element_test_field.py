# Generated by Django 2.1.3 on 2018-11-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0007_element_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='test_field',
        ),
    ]