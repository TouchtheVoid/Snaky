# Generated by Django 4.2.6 on 2023-11-16 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='cover',
            new_name='image',
        ),
    ]
