# Generated by Django 3.2.7 on 2021-10-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0014_alter_employee_variable_unconstant_arc_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_variable_constant',
            name='family_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_variable_constant',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_variable_constant',
            name='mothers_family_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_variable_constant',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee_variable_constant',
            name='pesel',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
