# Generated by Django 4.1.5 on 2023-02-20 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryptid_name', models.CharField(max_length=200)),
                ('aggressive', models.BooleanField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('continent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sighting_site', models.CharField(max_length=200)),
                ('sighting_date', models.DateTimeField(verbose_name='Happened in')),
                ('cryptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptids.cryptid')),
            ],
        ),
        migrations.AddField(
            model_name='cryptid',
            name='habitat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptids.habitat'),
        ),
    ]