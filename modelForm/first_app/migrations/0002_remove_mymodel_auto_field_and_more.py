# Generated by Django 5.0.6 on 2024-05-31 14:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='auto_field',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='big_integer_field',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='binary_field',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='boolean_field',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='char_field',
            field=models.CharField(default='Anne', max_length=100),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='date_field',
            field=models.DateField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='date_time_field',
            field=models.DateTimeField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='decimal_field',
            field=models.DecimalField(decimal_places=2, default='exit', max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='duration_field',
            field=models.DurationField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='email_field',
            field=models.EmailField(default='exit', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='float_field',
            field=models.FloatField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default='exit', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='integer_field',
            field=models.IntegerField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='positive_big_integer_field',
            field=models.PositiveBigIntegerField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='positive_integer_field',
            field=models.PositiveIntegerField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='positive_small_integer_field',
            field=models.PositiveSmallIntegerField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='small_integer_field',
            field=models.SmallIntegerField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='text_field',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='time_field',
            field=models.TimeField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='url_field',
            field=models.URLField(default='exit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='uuid_field',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]