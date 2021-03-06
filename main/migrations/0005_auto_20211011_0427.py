# Generated by Django 3.2.8 on 2021-10-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211007_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.CharField(max_length=100, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=150, null=True, verbose_name='Модель и Образ'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_title',
            field=models.CharField(max_length=100, null=True, verbose_name='Краткое описание'),
        ),
    ]
