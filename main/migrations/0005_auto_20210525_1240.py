# Generated by Django 3.2.3 on 2021-05-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210525_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='priceB',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trades',
            name='priceS',
            field=models.IntegerField(null=True),
        ),
    ]
