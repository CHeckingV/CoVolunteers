# Generated by Django 3.0.4 on 2020-03-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0006_helper_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
