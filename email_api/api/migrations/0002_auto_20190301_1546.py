# Generated by Django 2.0.13 on 2019-03-01 15:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='bcc',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='email',
            name='send_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]