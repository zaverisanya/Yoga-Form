# Generated by Django 4.1.4 on 2022-12-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_rename_payment_admission_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(blank=True, max_length=10, unique='True'),
        ),
    ]
