# Generated by Django 2.0.1 on 2018-02-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knuapp', '0011_auto_20180202_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announ_business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_chinese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_economics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_eng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_france',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_geography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_german',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_intrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_socialwelfare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_tourism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announ_tourismenglish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='lasted',
            field=models.CharField(default='18-02-03', max_length=128),
        ),
    ]
