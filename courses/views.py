from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course, Enrollment
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q, Count
import datetime
import calendar
from .serializers import CourseSerializer, ScheduleSerializer


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
        format_course_response(course)

    return Response(courses)


def format_course_response(course):
    course['schedule'] = (f'{course["schedule__days"]} '
            f'({course["schedule__start_time"].strftime("%H:%M")} - '
            f'{course["schedule__end_time"].strftime("%H:%M")})')
    course.pop('schedule__days')
    course.pop('schedule__start_time')
    course.pop('schedule__end_time')
    course['prerequisite_name'] = course['prerequisite__name']
    course.pop('prerequisite__name')


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])  
def registered_courses(request):
    if request.method == 'POST':
        return register_courses(request)
    
    return get_registered_course(request)


def register_courses(request):
    courses_codes = request.data
    registered_courses = Course.objects.values(
        'schedule__start_time', 'schedule__end_time', 'schedule__days'
    ).filter(enrollment__student=request.user)
    new_enrollments = []
    
    for course_code in courses_codes:
        if Enrollment.objects.filter(student_id=request.user.id, course_id=course_code).exists():
            return Response(
                'One or more of the given courses are already registered.', 
                status=status.HTTP_409_CONFLICT)
        
        try:
            course = Course.objects.get(pk=course_code)

        except Course.DoesNotExist:
            return Response(
                'One or more of the given courses are not found.', 
                status=status.HTTP_404_NOT_FOUND)

        for registered_course in registered_courses:
            if intersected(course, registered_course):
                return Response(
                    'One or more of the given courses intersect with the registered courses.', 
                    status=status.HTTP_409_CONFLICT)
            
        new_enrollments.append(Enrollment(student_id=request.user.id, course_id=course_code))
    
    Enrollment.objects.bulk_create(new_enrollments)
    return Response(status=status.HTTP_201_CREATED)


def intersected(course, registered_course):
    print(course.schedule)
    course_days = set(course.schedule.days.lower().split(', '))
    registered_course_days = set(registered_course['schedule__days'].lower().split(', '))
    
    # Days intersection
    if course_days.isdisjoint(registered_course_days):
        return False
    
    # Hours intersection
    return (
        course.schedule.start_time < registered_course['schedule__start_time'] and
        course.schedule.end_time > registered_course['schedule__start_time'] or
        registered_course['schedule__start_time'] < course.schedule.start_time and
        registered_course['schedule__end_time'] > course.schedule.start_time or
        course.schedule.start_time == registered_course['schedule__start_time'] and
        course.schedule.end_time == registered_course['schedule__end_time']
    )


def get_registered_course(request):
    registered_courses = Course.objects.values(
        'code', 'name', 'instructor', 'schedule__start_time', 'schedule__end_time', 'schedule__days', 
        'schedule__room_no'
    ).filter(enrollment__student=request.user)

    for course in registered_courses:
        format_registered_course(course)

    return Response(registered_courses)


def format_registered_course(course):
    course['time'] = (
        f'{course["schedule__start_time"].strftime("%H:%M")} - '
        f'{course["schedule__end_time"].strftime("%H:%M")}'
    )
    course['days'] = course['schedule__days']
    course['room_no'] = course['schedule__room_no']
    course.pop('schedule__room_no')
    course.pop('schedule__days')
    course.pop('schedule__start_time')
    course.pop('schedule__end_time')


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


@api_view(['POST'])
@permission_classes([IsAdminUser])  
def create_course(request):
    schedule = {
        'days': request.data.get('days'),
        'start_time': request.data.get('start_time'),
        'end_time': request.data.get('end_time'),
        'room_no': request.data.get('room_number')
    }
    schedule_serializer = ScheduleSerializer(data=schedule)

    if schedule_serializer.is_valid():
        created_schedule = schedule_serializer.save()
    else:
        return Response(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    course = {
        'code': request.data.get('code'),
        'name': request.data.get('name'),
        'instructor': request.data.get('instructor'),
        'description': request.data.get('description'),
        'prerequisite': request.data.get('prerequisite_course_code'),
        'capacity': request.data.get('capacity'),
        'schedule': created_schedule.id,
    }
    course_serializer = CourseSerializer(data=course)
    
    if course_serializer.is_valid():
        course_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)