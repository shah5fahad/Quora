# Generated by Django 5.2 on 2025-04-10 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='auther',
            new_name='author',
        ),
    ]
