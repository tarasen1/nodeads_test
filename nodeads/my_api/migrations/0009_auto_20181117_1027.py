# Generated by Django 2.1.3 on 2018-11-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0008_remove_element_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='checked',
            field=models.BooleanField(blank=True, default=None),
        ),
    ]
