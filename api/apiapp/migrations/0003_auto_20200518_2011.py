# Generated by Django 2.2.4 on 2020-05-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_remove_employees_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employees',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
    ]