# Generated by Django 5.0.1 on 2024-01-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0009_alter_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='payment_plan',
            field=models.TextField(),
        ),
    ]
