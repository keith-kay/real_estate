# Generated by Django 5.0.1 on 2024-02-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate_app', '0011_alter_property_payment_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(max_length=400),
        ),
    ]
