# Generated by Django 2.1.7 on 2019-07-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biotech', '0005_auto_20190710_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Place',
            field=models.TextField(default='none', max_length=200),
        ),
    ]