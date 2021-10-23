# Generated by Django 3.2 on 2021-10-23 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('rank', models.PositiveIntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('curved', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('row', models.PositiveIntegerField()),
                ('user', models.PositiveIntegerField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rank', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.rank')),
                ('section', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.section')),
            ],
        ),
    ]
