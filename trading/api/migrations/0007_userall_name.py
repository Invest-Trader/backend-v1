# Generated by Django 3.2.12 on 2022-02-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220227_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='userall',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
    ]
