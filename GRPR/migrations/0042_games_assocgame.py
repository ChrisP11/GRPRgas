# Generated by Django 4.2.16 on 2025-05-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRPR', '0041_games_format_games_min1_games_min18_games_numscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='AssocGame',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
