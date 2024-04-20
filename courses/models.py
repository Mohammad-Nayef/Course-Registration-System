from django.db import models
from django.contrib.auth.models import User


class CourseSchedule(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    days = models.CharField(max_length=70)
    startTime = models.TimeField()
    endTime = models.TimeField()
    roomNo = models.IntegerField()


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    prerequisiteCode = models.CharField(models.ForeignKey('self', on_delete=models.SET_NULL), max_length=20)
    instructor = models.CharField(max_length=50)
    capacity = models.IntegerField()
    scheduleId = models.IntegerField(models.ForeignKey(CourseSchedule, on_delete=models.SET_NULL))


class Enrollment(models.Model):
    studentId = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))
    courseId = models.IntegerField(models.ForeignKey(Course, on_delete=models.CASCADE))

    class Meta:
        unique_together = ('studentId', 'courseId')