# Generated by Django 2.0 on 2018-10-11 03:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_leakage_fragment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default=str(uuid.uuid1()), max_length=50, verbose_name='任务名'),
            preserve_default=False,
        ),
    ]
