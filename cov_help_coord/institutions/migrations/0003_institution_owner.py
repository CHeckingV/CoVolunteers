# Generated by Django 3.0.4 on 2020-03-20 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutions', '0002_remove_institution_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
    ]
