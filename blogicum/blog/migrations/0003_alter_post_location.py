# Generated by Django 3.2.16 on 2024-04-18 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240417_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.location', verbose_name='Местоположение'),
        ),
    ]
