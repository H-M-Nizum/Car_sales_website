# Generated by Django 5.0 on 2023-12-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car/uploads/'),
        ),
    ]
