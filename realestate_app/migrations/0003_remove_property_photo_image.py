# Generated by Django 5.0.1 on 2024-01-23 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0002_property_is_available_property_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='photo',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_photos/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate_app.property')),
            ],
        ),
    ]
