# Generated by Django 4.2.6 on 2023-11-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogpost_dislikes_blogpost_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]