# Generated by Django 2.1.7 on 2019-06-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Product_description',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='cart',
            name='Product_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
        ),
    ]