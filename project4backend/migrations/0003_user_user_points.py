# Generated by Django 3.2.7 on 2021-09-18 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4backend', '0002_reward_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_points',
            field=models.IntegerField(default=0),
        ),
    ]
