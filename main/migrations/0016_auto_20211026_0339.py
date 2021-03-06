# Generated by Django 3.2.8 on 2021-10-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211020_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('сountry', models.CharField(max_length=30, verbose_name='Страна')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('facebook', models.URLField(verbose_name='URl для facebook странице')),
                ('twitter', models.URLField(verbose_name='URl для twitter странице')),
                ('linkedin', models.URLField(verbose_name='URl для linkedin странице')),
                ('behance', models.URLField(verbose_name='URl для behance странице')),
            ],
            options={
                'verbose_name': 'Адрес',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('accessories', 'accessories'), ('shoes', 'shoes'), ('pants', 'pants'), ('outwear', 'outwear')], default='outwear', max_length=20),
        ),
    ]
