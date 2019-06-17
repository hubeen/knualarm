# Generated by Django 2.0.1 on 2018-02-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knuapp', '0013_announ_ars_announ_bme_announ_clas_announ_cm_announ_fan_announ_food_announ_forest_announ_hort_announ_'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announ_dhm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_dmrhim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_emt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='lasted',
            field=models.CharField(default='18-02-04', max_length=128),
        ),
    ]