# Generated by Django 2.1.7 on 2019-06-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20190621_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='role',
            field=models.CharField(choices=[('buyer', 'BUYER'), ('Flintwood_supplier', 'FLINTWOOD SUPPLIER'), ('btsupplier', 'BTTITAN SUPPLIER'), ('biotec_supplier', 'BIOTEC SUPPLIER')], default='buyer', max_length=30),
        ),
    ]