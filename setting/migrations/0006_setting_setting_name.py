# Generated by Django 4.2 on 2023-04-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0005_setting_auto_format_setting_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='setting_name',
            field=models.CharField(default='pen', max_length=100),
            preserve_default=False,
        ),
    ]