# Generated by Django 3.2.3 on 2021-05-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210525_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trades',
            name='profilePicture',
        ),
        migrations.AlterField(
            model_name='trades',
            name='quantity',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='trades',
            name='spent',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
