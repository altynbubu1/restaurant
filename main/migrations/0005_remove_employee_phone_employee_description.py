# Generated by Django 4.2.6 on 2023-10-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_employee_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание'),
        ),
    ]
