# Generated by Django 2.2.6 on 2020-01-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200105_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='genres',
            field=models.CharField(choices=[('Action', 'Action'), ('Thriller', 'Thriller'), ('Sci-Fi', 'Sci-Fi'), ('War', 'War'), ('Drama', 'Drama'), ('Crime', 'Crime')], max_length=50),
        ),
    ]