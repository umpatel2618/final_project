# Generated by Django 3.0.2 on 2020-02-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200225_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='closetime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='gym',
            name='opentime',
            field=models.TimeField(),
        ),
    ]
