# Generated by Django 4.0.2 on 2022-02-26 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0002_alter_token_assigned_date_alter_token_done_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='geo_latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='geo_longitude',
            new_name='lng',
        ),
    ]
