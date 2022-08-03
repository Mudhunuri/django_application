# Generated by Django 4.0.4 on 2022-07-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WO', models.CharField(max_length=20)),
                ('Com', models.CharField(max_length=20)),
                ('CMS', models.CharField(max_length=15)),
                ('Status', models.CharField(max_length=20)),
                ('CUName', models.CharField(max_length=20)),
                ('Scope', models.CharField(max_length=15)),
                ('R_T', models.CharField(max_length=20)),
                ('Smart_req', models.CharField(max_length=10)),
                ('smart', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
                ('Proc_req', models.CharField(max_length=15)),
                ('Proc_id', models.CharField(max_length=10)),
                ('Abbr_req', models.CharField(max_length=10)),
                ('Abbr_id', models.CharField(max_length=10)),
                ('Host_req', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]