# Generated by Django 4.1.5 on 2023-04-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_taker', '0009_alter_note_raw_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='raw_timestamp',
            field=models.IntegerField(default='0'),
        ),
    ]
