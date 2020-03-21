# Generated by Django 3.0.4 on 2020-03-21 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpers', '0002_helper_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helper',
            name='email',
        ),
        migrations.RemoveField(
            model_name='helper',
            name='owner',
        ),
        migrations.AlterField(
            model_name='helper',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='helper',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='helper',
            name='zipcode',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
