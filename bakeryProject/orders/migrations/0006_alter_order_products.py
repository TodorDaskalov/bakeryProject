# Generated by Django 4.2.3 on 2023-07-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.CharField(max_length=500),
        ),
    ]
