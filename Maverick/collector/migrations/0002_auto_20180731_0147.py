# Generated by Django 2.0.2 on 2018-07-31 06:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField()),
                ('date', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='phones',
        ),
        migrations.AddField(
            model_name='collector',
            name='scheduler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Scheduler'),
        ),
    ]
