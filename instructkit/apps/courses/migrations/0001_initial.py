# Generated by Django 2.0.3 on 2019-11-29 22:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration_type', models.CharField(choices=[('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], default='days', help_text='Default is days. Set to hours, weeks, months.', max_length=20)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('category', models.CharField(choices=[('homework', 'Homework'), ('project', 'Project'), ('exercise', 'Exercise')], max_length=300)),
                ('url', models.URLField()),
                ('document', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration_type', models.CharField(choices=[('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], default='days', help_text='Default is days. Set to hours, weeks, months.', max_length=20)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('instructors', models.ManyToManyField(related_name='courses', to='accounts.Instructor')),
                ('students', models.ManyToManyField(related_name='courses', to='accounts.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration_type', models.CharField(choices=[('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], default='days', help_text='Default is days. Set to hours, weeks, months.', max_length=20)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('instructor', models.ForeignKey(help_text='The instructor for this lesson.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='lessons', to='accounts.Instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration_type', models.CharField(choices=[('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')], default='days', help_text='Default is days. Set to hours, weeks, months.', max_length=20)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('level', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('medium', 'Medium'), ('high', 'High')], help_text='The level of relative difficulty of the material.', max_length=300)),
                ('course', models.ForeignKey(help_text='The course associated with this module.', on_delete=django.db.models.deletion.CASCADE, related_name='units', to='courses.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(help_text='The unit this lesson belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Unit'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='lesson',
            field=models.ForeignKey(help_text='The lesson this assignment relates to.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignments', to='courses.Lesson'),
        ),
    ]
