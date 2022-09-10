# Generated by Django 4.0.6 on 2022-09-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ledger_name', models.CharField(max_length=255)),
                ('Opening_balance', models.IntegerField()),
                ('Type', models.CharField(blank=True, default='Dr', max_length=255, null=True)),
            ],
        ),
    ]