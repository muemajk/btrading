# Generated by Django 2.1.7 on 2019-06-21 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biotechorders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flintwoodorders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tktitanorders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='biotechorders',
            name='OrderList',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='biotechorders',
            name='Order_Payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='flintwoodorders',
            name='OrderList',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='flintwoodorders',
            name='Order_Payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tktitanorders',
            name='OrderList',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='tktitanorders',
            name='Order_Payment',
            field=models.BooleanField(default=False),
        ),
    ]