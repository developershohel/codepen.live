# Generated by Django 4.2 on 2023-04-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0006_setting_setting_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='auto_format',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='auto_run',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='auto_save',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]