# Generated by Django 5.0.1 on 2024-03-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_remove_doorblock_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='opening_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frame',
            name='opening_type2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
