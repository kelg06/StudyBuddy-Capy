# Generated by Django 5.1.2 on 2025-04-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_grouppost_delete_class_profile_is_group_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='declined',
            field=models.BooleanField(default=False),
        ),
    ]
