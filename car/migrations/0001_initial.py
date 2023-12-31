# Generated by Django 5.0 on 2023-12-15 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=15)),
                ('quantity', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brandmodel')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
