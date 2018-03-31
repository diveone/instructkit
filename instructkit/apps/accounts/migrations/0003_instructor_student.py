# Generated by Django 2.0.3 on 2018-03-31 18:26

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180331_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('skills', models.CharField(max_length=1000)),
                ('speciality', models.CharField(choices=[('frontend dev', 'Frontend Web Development'), ('backend dev', 'Backend Web Development'), ('dev ops', 'Dev Operations (devOps)'), ('user experience', 'User Experience & Interfaces'), ('full stack', 'Full Stack Web Development')], max_length=255)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('outcome', models.CharField(choices=[('full-time work', 'Full-time Employment'), ('part-time work', 'Part-time Employment'), ('independent work', 'Independent Work'), ('entrepreneur', 'Start-up/Entrepreneur'), ('education', 'Education Goal')], max_length=255)),
                ('outcome_status', models.CharField(choices=[('on track', 'On track for course completion'), ('needs support', 'Requires additional support'), ('off track', 'Will not complete the course')], max_length=255)),
                ('notes', models.TextField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
