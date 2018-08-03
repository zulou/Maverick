# Generated by Django 2.0.2 on 2018-08-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_auto_20180801_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collector',
            name='type',
        ),
        migrations.AddField(
            model_name='scheduler',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]
