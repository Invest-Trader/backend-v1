# Generated by Django 3.2.12 on 2022-02-27 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMetaData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ip', models.CharField(blank=True, max_length=20, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=50, null=True)),
                ('os', models.CharField(blank=True, max_length=50, null=True)),
                ('device', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('pancard_number', models.CharField(blank=True, max_length=11, null=True)),
                ('additional_documents', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'AADHAR CARD'), (1, 'PASSPORT'), (2, 'DRIVING LICENSE'), (3, 'OTHER')], default=0, null=True)),
                ('additional_documents_number', models.CharField(blank=True, max_length=18, null=True)),
                ('pancard_image', models.ImageField(blank=True, upload_to='images/documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAll',
            fields=[
                ('id', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('phoneno', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('day', models.CharField(blank=True, default='', max_length=3, null=True)),
                ('month', models.CharField(blank=True, default='', max_length=3, null=True)),
                ('year', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'NOT_PROVIDED'), (1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], default=0, null=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('account_verfication', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'VERIFIED'), (1, 'NOT VERIFIED'), (2, 'IN PROCESS'), (3, 'BLOCKED')], default=0, null=True)),
                ('email_verfication', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'VERIFIED'), (1, 'NOT VERIFIED')], default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccountFund',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
