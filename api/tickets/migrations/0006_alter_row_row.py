# Generated by Django 3.2 on 2021-10-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20211021_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='row',
            field=models.IntegerField(),
        ),
    ]