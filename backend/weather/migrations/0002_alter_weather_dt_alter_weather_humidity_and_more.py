# Generated by Django 4.2.3 on 2023-09-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='dt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temp',
            field=models.FloatField(),
        ),
    ]
