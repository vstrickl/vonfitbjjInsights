# Generated by Django 5.0.6 on 2024-06-02 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metainsights', '0005_facebooktoken_created_at_facebooktoken_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('category_list', models.JSONField()),
            ],
        ),
    ]