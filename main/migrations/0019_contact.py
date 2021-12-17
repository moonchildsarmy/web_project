# Generated by Django 3.2.8 on 2021-10-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_product_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_position', models.DecimalField(decimal_places=3, max_digits=10)),
                ('lat_position', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
