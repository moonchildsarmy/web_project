# Generated by Django 4.0 on 2021-12-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('outwear', 'outwear'), ('pants', 'pants'), ('accessories', 'accessories'), ('shoes', 'shoes')], default='outwear', max_length=20),
        ),
    ]
