from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count, F


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_by_code(request, code):
    try:
        course = Course.objects.values(
            'code', 'name', 'instructor', 'description', 'schedule__days', 'schedule__start_time', 
            'schedule__end_time', 'capacity', enrollments_count=Count('enrollment'), 
            prerequisite_name=F('prerequisite__name')
        ).get(pk=code)
        
    except Course.DoesNotExist:
        return Response(
            {'error': f'Course with code \'{code}\' is not found.'}, 
            status=status.HTTP_404_NOT_FOUND)
    
    format_schedule(course)

    return Response(course)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_courses(request):
    query = request.GET['query']
    courses = Course.objects.values(
            'code', 'name', 'instructor', 'schedule__days', 'schedule__start_time', 
            'schedule__end_time', 'capacity', enrollments_count=Count('enrollment')
        ).filter(
        Q(code__icontains=query) | Q(name__icontains=query) | Q(instructor__icontains=query)
    )
    
    for course in courses:
        format_schedule(course)

    return Response(courses)


def format_schedule(course):
    course['schedule'] = (f'{course["schedule__days"]} '
            f'({course["schedule__start_time"].strftime("%H:%M")} - {course["schedule__end_time"].strftime("%H:%M")})')
    course.pop('schedule__days')
    course.pop('schedule__start_time')
    course.pop('schedule__end_time')