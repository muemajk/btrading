# Generated by Django 2.1.7 on 2019-07-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flintwood', '0005_auto_20190627_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Catergory',
            field=models.CharField(default='fresh_food', max_length=254),
        ),
    ]
