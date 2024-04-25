from django.db import models
from django.contrib.auth.models import User


class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=70)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.IntegerField()

    class Meta:
        db_table = 'courses_schedules'


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    prerequisite = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    instructor = models.CharField(max_length=50)
    capacity = models.IntegerField()
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'courses'


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'enrollments'
        unique_together = ('student', 'course')