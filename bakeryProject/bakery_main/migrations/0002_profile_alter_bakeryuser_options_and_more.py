# Generated by Django 4.2.3 on 2023-07-06 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='bakeryuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='bakeryuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='bakeryuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='bakeryuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='bakeryuser',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery_main.profile'),
        ),
    ]
