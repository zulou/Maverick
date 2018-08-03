# Generated by Django 2.0.2 on 2018-08-02 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_auto_20180801_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='state',
            field=models.IntegerField(default=django.utils.timezone.now),
        ),
    ]