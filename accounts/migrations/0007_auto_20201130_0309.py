# Generated by Django 3.1.3 on 2020-11-29 21:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201130_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgdata',
            name='myfile',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
