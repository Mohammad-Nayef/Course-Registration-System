from django.db import models
from django.contrib.auth.models import User


class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=70)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.IntegerField()

    class Meta:
        db_table = 'CoursesSchedules'


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200)
    prerequisite_code = models.CharField(models.ForeignKey('self', on_delete=models.SET_NULL), max_length=20, null=True)
    instructor = models.CharField(max_length=50)
    capacity = models.IntegerField()
    schedule_id = models.IntegerField(models.ForeignKey(CourseSchedule, on_delete=models.SET_NULL))

    class Meta:
        db_table = 'Courses'


class Enrollment(models.Model):
    student_id = models.IntegerField(models.ForeignKey(User, on_delete=models.CASCADE))
    course_code = models.CharField(models.ForeignKey(Course, on_delete=models.CASCADE), max_length=20)

    class Meta:
        db_table = "Enrollments"
        unique_together = ('student_id', 'course_code')