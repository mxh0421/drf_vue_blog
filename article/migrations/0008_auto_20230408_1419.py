# Generated by Django 3.1.3 on 2023-04-08 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20230406_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id']},
        ),
    ]
