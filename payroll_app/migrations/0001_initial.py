# Generated by Django 3.2.4 on 2021-09-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Variable_Constant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesel', models.CharField(max_length=11)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=50)),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('family_name', models.CharField(max_length=50)),
                ('mothers_family_name', models.CharField(max_length=50)),
                ('date_of_entry', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]