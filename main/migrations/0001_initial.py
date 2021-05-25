# Generated by Django 3.2.3 on 2021-05-25 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=10)),
                ('priceB', models.CharField(max_length=15)),
                ('priceS', models.CharField(max_length=15)),
                ('quantity', models.CharField(max_length=15)),
                ('spent', models.CharField(max_length=15)),
                ('profilePicture', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]