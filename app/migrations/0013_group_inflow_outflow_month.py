# Generated by Django 4.0.6 on 2022-09-13 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_cash_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_inflow_outflow',
            name='month',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.months'),
            preserve_default=False,
        ),
    ]
