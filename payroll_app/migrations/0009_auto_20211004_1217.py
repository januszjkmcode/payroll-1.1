# Generated by Django 3.2.4 on 2021-10-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0008_auto_20211004_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_variable_unconstant_arc',
            name='date_of_exit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee_variable_unconstant_arc',
            name='date_of_entry',
            field=models.DateTimeField(),
        ),
    ]