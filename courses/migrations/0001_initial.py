# Generated by Django 5.0.4 on 2024-04-25 09:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=70)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room_no', models.IntegerField()),
            ],
            options={
                'db_table': 'courses_schedules',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('prerequisite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.courseschedule')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'enrollments',
                'unique_together': {('student', 'course')},
            },
        ),
    ]
