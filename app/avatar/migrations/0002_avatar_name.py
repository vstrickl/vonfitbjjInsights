# Generated by Django 5.0.6 on 2024-06-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]