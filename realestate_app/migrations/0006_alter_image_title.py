# Generated by Django 5.0.1 on 2024-01-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0005_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
    ]
