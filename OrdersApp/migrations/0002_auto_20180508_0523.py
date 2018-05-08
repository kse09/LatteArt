# Generated by Django 2.0.3 on 2018-05-08 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrdersApp.Branch'),
        ),
        migrations.AddField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OrdersApp.CustomerProfile'),
        ),
    ]
