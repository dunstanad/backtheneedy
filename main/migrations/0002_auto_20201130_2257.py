# Generated by Django 3.1.3 on 2020-11-30 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='suggestions',
            new_name='sugg',
        ),
    ]
