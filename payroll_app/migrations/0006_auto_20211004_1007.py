# Generated by Django 3.2.4 on 2021-10-04 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0005_profession_type_of_change'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='type_of_change',
        ),
        migrations.AddField(
            model_name='profession_arc',
            name='type_of_change',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
