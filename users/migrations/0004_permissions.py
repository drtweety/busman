# Generated by Django 3.1.2 on 2020-10-27 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20201025_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_permissions', models.SmallIntegerField(choices=[(0, 'Restrict'), (1, 'Allow')], default=0)),
                ('product_permissions', models.SmallIntegerField(choices=[(0, 'None'), (1, 'View'), (2, 'View, Create, Modify'), (3, 'View, Create, Modify, Delete')], default=0)),
                ('sales_permissions', models.SmallIntegerField(choices=[(0, 'None'), (1, 'View'), (2, 'View, Create, Modify'), (3, 'View, Create, Modify, Delete')], default=0)),
                ('purchase_permissions', models.SmallIntegerField(choices=[(0, 'None'), (1, 'View'), (2, 'View, Create, Modify'), (3, 'View, Create, Modify, Delete')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
