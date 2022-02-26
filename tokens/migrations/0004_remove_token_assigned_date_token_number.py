# Generated by Django 4.0.2 on 2022-02-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0003_rename_geo_latitude_token_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='assigned_date',
        ),
        migrations.AddField(
            model_name='token',
            name='number',
            field=models.TextField(default=0, max_length=14),
            preserve_default=False,
        ),
    ]