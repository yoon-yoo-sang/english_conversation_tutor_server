# Generated by Django 4.2.7 on 2023-11-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
