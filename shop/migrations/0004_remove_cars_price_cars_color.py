# Generated by Django 4.2.7 on 2023-11-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_cars_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='price',
        ),
        migrations.AddField(
            model_name='cars',
            name='color',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
