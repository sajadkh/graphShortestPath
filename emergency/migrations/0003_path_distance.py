# Generated by Django 2.1.5 on 2019-01-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0002_auto_20190127_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='distance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
