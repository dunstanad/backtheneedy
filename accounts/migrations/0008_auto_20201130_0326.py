# Generated by Django 3.1.3 on 2020-11-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201130_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgdata',
            name='myfile',
            field=models.ImageField(default='False', upload_to='media'),
        ),
    ]
