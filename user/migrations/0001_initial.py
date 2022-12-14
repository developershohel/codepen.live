# Generated by Django 4.0.3 on 2022-08-04 23:09

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and _ only.', max_length=100, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(help_text='<ul><li>The password length must be greater than or equal 8</li><li>The password must contain one or more uppercase and lowercase characters</li><li>The password must contain one or more special characters</li></ul>', max_length=255)),
                ('first_name', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and whitespace only.', max_length=100)),
                ('last_name', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and whitespace only.', max_length=100)),
                ('user_type', models.IntegerField(default=0)),
                ('user_trail', models.BooleanField(default=False)),
                ('user_status', models.BooleanField(default=False)),
                ('user_activation_key', models.CharField(blank=True, max_length=255)),
                ('user_verification_code', models.IntegerField(blank=True)),
                ('user_registered', models.DateTimeField(auto_now_add=True)),
                ('user_modified', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('follower', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_blocked', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_country', models.CharField(blank=True, max_length=100, null=True)),
                ('user_city', models.CharField(blank=True, max_length=100, null=True)),
                ('user_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('user_login', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
