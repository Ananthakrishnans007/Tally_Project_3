# Generated by Django 4.0.6 on 2022-09-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_ledger_vouchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='Type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
