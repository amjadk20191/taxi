# Generated by Django 4.2.4 on 2023-08-18 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='dtae',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='end_d',
            field=models.TextField(default='saassas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_d',
            field=models.TextField(default='ssssssssssssssssssssss'),
            preserve_default=False,
        ),
    ]
