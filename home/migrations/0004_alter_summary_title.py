# Generated by Django 5.1.4 on 2025-03-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_summarie_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
