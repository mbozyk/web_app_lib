# Generated by Django 3.0.5 on 2020-05-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200503_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='*', max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='*', max_length=100),
        ),
    ]