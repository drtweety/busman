# Generated by Django 3.1.1 on 2020-09-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20200923_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='discout',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
