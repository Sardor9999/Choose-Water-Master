# Generated by Django 3.1.4 on 2022-03-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220310_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrival_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='selling_price',
            field=models.FloatField(default=0),
        ),
    ]
