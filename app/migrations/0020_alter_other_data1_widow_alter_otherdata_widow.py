# Generated by Django 4.0.5 on 2022-08-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0019_other_data1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_data1',
            name='widow',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='otherdata',
            name='widow',
            field=models.CharField(max_length=10),
        ),
    ]