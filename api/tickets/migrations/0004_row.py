# Generated by Django 3.2 on 2021-10-21 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20211021_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(unique=True)),
                ('section', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.section')),
            ],
        ),
    ]
