# Generated by Django 4.2.11 on 2024-06-14 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_spouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('related', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('couple_name', models.CharField(max_length=80)),
                ('wedding_date', models.DateField()),
                ('speech_length', models.CharField(max_length=50)),
                ('history', models.TextField(blank=True, null=True)),
                ('mentions', models.TextField(blank=True, null=True)),
                ('thanks', models.TextField(blank=True, null=True)),
                ('additonal_preferences', models.TextField(blank=True, null=True)),
                ('dos_donts', models.TextField(blank=True, null=True)),
                ('attendees', models.CharField(blank=True, max_length=50, null=True)),
                ('ages', models.CharField(blank=True, max_length=50, null=True)),
                ('tone_emotional', models.BooleanField(default=False)),
                ('tone_heartfelt', models.BooleanField(default=False)),
                ('tone_inspirational', models.BooleanField(default=False)),
                ('tone_happy', models.BooleanField(default=False)),
                ('tone_funny', models.BooleanField(default=False)),
                ('tone_formal', models.BooleanField(default=False)),
                ('tone_casual', models.BooleanField(default=False)),
                ('tone_motivational', models.BooleanField(default=False)),
                ('tone_reflective', models.BooleanField(default=False)),
                ('tone_others', models.CharField(blank=True, max_length=100, null=True)),
                ('user_input', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
    ]
