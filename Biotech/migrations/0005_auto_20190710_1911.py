# Generated by Django 2.1.7 on 2019-07-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biotech', '0004_auto_20190628_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Catergory',
            field=models.CharField(default='Medicine', max_length=254),
        ),
    ]
