# Generated by Django 5.0.1 on 2024-01-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_doorblock_opening_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doorblock',
            name='opening_type',
        ),
    ]