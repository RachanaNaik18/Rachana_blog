# Generated by Django 5.0 on 2023-12-12 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='user',
        ),
    ]