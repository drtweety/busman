# Generated by Django 3.1.1 on 2020-09-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20200924_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.BooleanField(choices=[(0, 'Pending'), (1, 'Completed')], default=0, max_length=20),
        ),
    ]
