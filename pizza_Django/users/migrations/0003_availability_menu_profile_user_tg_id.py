# Generated by Django 5.1.7 on 2025-04-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('salyami', models.IntegerField()),
                ('tomato_sauce', models.IntegerField()),
                ('cheese', models.IntegerField()),
                ('species', models.IntegerField()),
                ('bazilik', models.IntegerField()),
                ('ham', models.IntegerField()),
                ('ananas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salyami', models.BooleanField()),
                ('tomato_sauce', models.BooleanField()),
                ('cheese', models.BooleanField()),
                ('species', models.BooleanField()),
                ('bazilik', models.BooleanField()),
                ('ham', models.BooleanField()),
                ('ananas', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user_tg_id',
            field=models.IntegerField(default=None),
        ),
    ]
