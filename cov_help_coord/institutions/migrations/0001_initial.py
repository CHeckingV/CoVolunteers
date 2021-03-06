# Generated by Django 3.0.4 on 2020-03-20 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('ansprechpartner', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('companytype', models.CharField(choices=[('SUP', 'Supermarkt'), ('HOS', 'Krankenhaus'), ('FAR', 'Landwirt'), ('CAR', 'Pflege')], default='SUP', max_length=3)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
