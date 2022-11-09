# Generated by Django 4.0.3 on 2022-08-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('cats_register', models.DateTimeField(auto_now_add=True, null=True)),
                ('cats_modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]