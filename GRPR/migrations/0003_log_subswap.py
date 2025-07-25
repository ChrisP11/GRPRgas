# Generated by Django 4.2.16 on 2024-12-16 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRPR', '0002_alter_teetimesind_courseid_alter_teetimesind_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SentDate', models.DateTimeField()),
                ('Type', models.CharField(max_length=256)),
                ('MessageID', models.CharField(max_length=256)),
                ('RequestDate', models.DateTimeField()),
                ('OfferID', models.IntegerField()),
                ('ReceiveID', models.IntegerField()),
                ('RefID', models.IntegerField()),
                ('Msg', models.CharField(max_length=1024)),
                ('Status', models.IntegerField()),
                ('To_number', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Log',
            },
        ),
        migrations.CreateModel(
            name='SubSwap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestDate', models.DateTimeField()),
                ('PID', models.IntegerField()),
                ('TeeTimeIndID', models.IntegerField()),
                ('Type', models.CharField(max_length=32)),
                ('Status', models.CharField(max_length=32)),
                ('Msg', models.CharField(max_length=2048)),
                ('OtherPlayers', models.CharField(max_length=1024)),
                ('SwapID', models.IntegerField()),
            ],
            options={
                'db_table': 'SubSwap',
            },
        ),
    ]
