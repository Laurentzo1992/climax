# Generated by Django 5.0.3 on 2024-04-01 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('created', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('libelle', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('created', models.DateField(auto_created=True, auto_now_add=True, null=True)),
                ('nom', models.CharField(blank=True, max_length=20, null=True)),
                ('prenom', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('sal_employee', models.CharField(blank=True, max_length=20, null=True)),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profession')),
            ],
        ),
    ]
