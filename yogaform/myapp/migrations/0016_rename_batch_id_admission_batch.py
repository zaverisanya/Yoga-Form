# Generated by Django 4.1.4 on 2022-12-12 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_batch_batch_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='batch_id',
            new_name='batch',
        ),
    ]
