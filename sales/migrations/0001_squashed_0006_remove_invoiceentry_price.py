# Generated by Django 3.1.1 on 2020-09-23 04:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('sales', '0001_initial'), ('sales', '0002_auto_20200918_0938'), ('sales', '0003_auto_20200918_1348'), ('sales', '0004_auto_20200920_1408'), ('sales', '0005_invoiceentry_price'), ('sales', '0006_remove_invoiceentry_price')]

    initial = True

    dependencies = [
        ('products', '0007_auto_20200916_1308'),
        ('organization', '0004_auto_20200914_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='organization.organization')),
                ('date', models.DateField(default=datetime.datetime(2020, 9, 18, 13, 48, 14, 753274, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='sales.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_invoices', to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Invoice Entries',
            },
        ),
    ]
