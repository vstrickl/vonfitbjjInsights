# Generated by Django 5.0.6 on 2024-06-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metainsights', '0006_facebookpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpage',
            name='cli_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
