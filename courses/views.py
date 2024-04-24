from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, CourseSchedule, Enrollment
from django.forms.models import model_to_dict  
from rest_framework import status

@api_view(['GET'])
def get_course_details(request, code):
    try:
        course = Course.objects.get(code=code)

    except Course.DoesNotExist:
        return Response(data=f'Course with code {code} is not found.', status=status.HTTP_404_NOT_FOUND)

    schedule = CourseSchedule.objects.get(id=course.schedule_id)
    enrollments_count = Enrollment.objects.filter(course_code=course.code).count()
    prerequisite = None

    if course.prerequisite_code is not None:
        prerequisite_course = Course.objects.get(code=course.prerequisite_code)
        prerequisite = {
            'code': prerequisite_course.code,
            'name': prerequisite_course.name
        }
    
    course = {
            'code': course.code,
            'name': course.name,
            'instructor': course.instructor,
            'capacity': course.capacity,
            'enrollmentsCount': enrollments_count,
            'schedule': f'{schedule.days} ({schedule.start_time} - {schedule.end_time})',
            'description': course.description,
            'prerequisite': prerequisite
    }

    return Response(course)