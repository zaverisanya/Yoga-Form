# Generated by Django 4.1.4 on 2022-12-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_batch_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
