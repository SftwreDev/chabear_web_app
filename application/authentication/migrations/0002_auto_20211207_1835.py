# Generated by Django 3.2.8 on 2021-12-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Contact Number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='First Name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Last Name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
