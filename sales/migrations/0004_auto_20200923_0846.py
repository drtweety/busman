# Generated by Django 3.1.1 on 2020-09-23 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_invoice_discout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='discout',
            new_name='discount',
        ),
    ]