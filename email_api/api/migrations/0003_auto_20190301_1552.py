# Generated by Django 2.0.13 on 2019-03-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190301_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='reply_to',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]