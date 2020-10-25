# Generated by Django 3.1.2 on 2020-10-25 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0005_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
