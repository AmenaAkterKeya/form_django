# Generated by Django 5.0.6 on 2024-05-31 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_remove_mymodel_auto_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='slug_field',
            field=models.SlugField(default='exit'),
            preserve_default=False,
        ),
    ]
