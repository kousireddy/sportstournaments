# Generated by Django 5.2.3 on 2025-06-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('couch', models.CharField(max_length=255)),
            ],
        ),
    ]
