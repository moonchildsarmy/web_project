# Generated by Django 3.2.8 on 2021-10-18 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20211018_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('shoes', 'shoes'), ('outwear', 'outwear'), ('accessories', 'accessories'), ('pants', 'pants')], default='outwear', max_length=20),
        ),
    ]
