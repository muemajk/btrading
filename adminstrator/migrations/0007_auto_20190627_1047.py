# Generated by Django 2.1.7 on 2019-06-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator', '0006_auto_20190624_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='freightrate',
            name='Destinationothertax',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='freightrate',
            name='Sourceothertax',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='Destinationtax',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='MarkupRate',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='QuantityRecieved',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='QuantitySent',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='Sourcetax',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='Total_cost',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='freightrate',
            name='Unit_cost',
            field=models.IntegerField(default=1),
        ),
    ]