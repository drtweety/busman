# Generated by Django 3.1.1 on 2020-09-27 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_minimum_price'),
        ('sales', '0016_auto_20200927_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoiceentry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]