# Generated by Django 3.0.4 on 2020-03-21 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutions', '0004_institution_helpers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institutions', to=settings.AUTH_USER_MODEL),
        ),
    ]
