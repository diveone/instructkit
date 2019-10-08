# Generated by Django 2.0.3 on 2018-11-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180401_0547'),
        ('courses', '0002_auto_20181025_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', to='accounts.Student'),
        ),
    ]
