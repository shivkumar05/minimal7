# Generated by Django 4.0.1 on 2022-12-09 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_profile_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_pic',
            name='Post',
        ),
    ]
