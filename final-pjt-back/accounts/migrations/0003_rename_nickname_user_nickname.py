# Generated by Django 3.2.13 on 2022-11-17 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nickName',
            new_name='nickname',
        ),
    ]