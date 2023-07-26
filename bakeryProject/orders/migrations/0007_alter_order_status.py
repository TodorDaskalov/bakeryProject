# Generated by Django 4.2.3 on 2023-07-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('received', 'Received'), ('working', 'Working on it'), ('ready_to_pickup', 'Ready to pickup'), ('done', 'Done')], default='received', max_length=20),
        ),
    ]