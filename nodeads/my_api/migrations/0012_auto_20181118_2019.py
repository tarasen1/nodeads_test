# Generated by Django 2.1.3 on 2018-11-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0011_auto_20181117_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]