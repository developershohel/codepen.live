# Generated by Django 4.2 on 2023-04-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='html',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
