# Generated by Django 5.0.1 on 2024-01-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorblock',
            name='opening_type',
            field=models.IntegerField(),
        ),
    ]