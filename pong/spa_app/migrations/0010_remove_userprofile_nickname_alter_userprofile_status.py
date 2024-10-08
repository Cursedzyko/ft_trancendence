# Generated by Django 4.2.9 on 2024-08-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa_app', '0009_userprofile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('in_game', 'In Game'), ('offline', 'Offline'), ('online', 'Online')], default='offline', max_length=10),
        ),
    ]
