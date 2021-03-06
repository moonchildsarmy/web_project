# Generated by Django 3.2.8 on 2021-10-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211018_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('size', models.CharField(max_length=50, verbose_name='Размер')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=50, null=True, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('accessories', 'accessories'), ('shoes', 'shoes'), ('pants', 'pants'), ('outwear', 'outwear')], default='outwear', max_length=20),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.product'),
        ),
    ]
