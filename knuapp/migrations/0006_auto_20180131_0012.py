# Generated by Django 2.0.1 on 2018-01-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knuapp', '0005_auto_20180131_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='lasted',
            field=models.CharField(max_length=128),
        ),
    ]
