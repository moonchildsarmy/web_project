# Generated by Django 4.0 on 2021-12-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('shoes', 'shoes'), ('outwear', 'outwear'), ('pants', 'pants'), ('accessories', 'accessories')], default='outwear', max_length=20),
        ),
    ]