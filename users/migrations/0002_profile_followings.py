# Generated by Django 3.2.6 on 2021-08-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to='users.Profile'),
        ),
    ]