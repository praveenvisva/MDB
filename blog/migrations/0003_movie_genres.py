# Generated by Django 2.2.6 on 2020-01-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200104_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(choices=[('Action', 'Action'), ('Thriller', 'Thriller'), ('Sci-Fi', 'Sci-Fi'), ('War', 'War'), ('Romance', 'Romance'), ('Drama', 'Drama')], default='Action', max_length=50),
        ),
    ]
