# Generated by Django 3.2.3 on 2021-05-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210525_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trades',
            name='priceB',
        ),
        migrations.RemoveField(
            model_name='trades',
            name='priceS',
        ),
        migrations.AlterField(
            model_name='trades',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='spent',
            field=models.IntegerField(blank=True, max_length=15),
        ),
    ]
