# Generated by Django 2.1.3 on 2018-11-13 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0004_auto_20181113_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent_group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_api.Group'),
        ),
    ]
