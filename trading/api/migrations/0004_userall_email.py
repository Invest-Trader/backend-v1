# Generated by Django 3.2.12 on 2022-02-27 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220227_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='userall',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]