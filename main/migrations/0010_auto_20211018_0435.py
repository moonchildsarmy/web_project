# Generated by Django 3.2.8 on 2021-10-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211015_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('outwear', 'outwear'), ('pants', 'pants'), ('shoes', 'shoes'), ('accessories', 'accessories')], default='outwear', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]