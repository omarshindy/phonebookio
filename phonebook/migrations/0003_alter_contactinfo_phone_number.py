# Generated by Django 4.1.5 on 2023-01-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_contactinfo_delete_mobileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
