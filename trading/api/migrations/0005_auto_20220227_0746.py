# Generated by Django 3.2.12 on 2022-02-27 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userall_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userall',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='userall',
            name='lname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]