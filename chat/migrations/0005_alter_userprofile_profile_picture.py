# Generated by Django 4.2.3 on 2023-08-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
