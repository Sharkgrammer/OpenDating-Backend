# Generated by Django 5.1.2 on 2024-10-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_stat_top_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='top_interests',
            field=models.JSONField(blank=True),
        ),
    ]
