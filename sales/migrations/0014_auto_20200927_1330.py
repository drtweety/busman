# Generated by Django 3.1.1 on 2020-09-27 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20200914_0713'),
        ('products', '0003_product_minimum_price'),
        ('sales', '0013_auto_20200924_1009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoice',
            new_name='SalesInvoice',
        ),
        migrations.RenameModel(
            old_name='InvoiceEntry',
            new_name='SalesInvoiceEntry',
        ),
        migrations.AlterModelOptions(
            name='salesinvoiceentry',
            options={'verbose_name_plural': 'Sales Invoice Entries'},
        ),
    ]