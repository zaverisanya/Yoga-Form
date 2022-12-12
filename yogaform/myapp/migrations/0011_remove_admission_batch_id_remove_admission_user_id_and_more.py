# Generated by Django 4.1.4 on 2022-12-11 17:39

import django.core.validators
from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='batch_id',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(validators=[myapp.models.validate_age]),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, max_length=17, unique='True', validators=[django.core.validators.RegexValidator(message='Enter a valid contact number', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]