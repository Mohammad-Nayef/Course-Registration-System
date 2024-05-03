from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course, Enrollment
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
import datetime
import calendar


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_courses(request):
    query = request.GET['query']
    courses = Course.objects.values(
            'code', 'name', 'instructor', 'description', 'prerequisite__name', 'schedule__days', 
            'schedule__start_time', 'schedule__end_time', 'capacity', 
            enrollments_count=Count('enrollment')
        ).filter(
        Q(code__icontains=query) | Q(name__icontains=query) | Q(instructor__icontains=query)
    )
    
    for course in courses:
        format_schedule(course)

    return Response(courses)


def format_schedule(course):
    course['schedule'] = (f'{course["schedule__days"]} '
            f'({course["schedule__start_time"].strftime("%H:%M")} - '
            f'{course["schedule__end_time"].strftime("%H:%M")})')
    course.pop('schedule__days')
    course.pop('schedule__start_time')
    course.pop('schedule__end_time')
    course['prerequisite_name'] = course['prerequisite__name']
    course.pop('prerequisite__name')


@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def register_course(request):
    courses_codes = request.data
    new_enrollments = []

    for course_code in courses_codes:
        if Enrollment.objects.filter(student_id=request.user.id, course_id=course_code).exists():
            return Response(
                {'error': 'At least one course is already registered.'}, 
                status=status.HTTP_409_CONFLICT)
        
        if not Course.objects.filter(code=course_code).exists():
            return Response(
                {'error': 'At least one course is not found.'}, 
                status=status.HTTP_404_NOT_FOUND)

        new_enrollments.append(Enrollment(student_id=request.user.id, course_id=course_code))
    
    Enrollment.objects.bulk_create(new_enrollments)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_notifications(request):
    registered_courses = Course.objects.values(
            'name', 'schedule__start_time', 'schedule__end_time', 'schedule__days'
        ).filter(enrollment__student=request.user)
    
    today_index = datetime.datetime.now().weekday()
    today = calendar.day_name[today_index]
    result = []

    for course in registered_courses:
        if today.lower() in course['schedule__days'].lower():
            result.append(f'You have {course["name"]} lecture today from '
                f'{course["schedule__start_time"].strftime("%H:%M")} to '
                f'{course["schedule__end_time"].strftime("%H:%M")}.')

    return Response(result)