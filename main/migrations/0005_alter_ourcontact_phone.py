# Generated by Django 5.2.4 on 2025-07-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ourcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourcontact',
            name='phone',
            field=models.CharField(max_length=18),
        ),
    ]
