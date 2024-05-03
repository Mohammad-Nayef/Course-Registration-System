# System APIs
```http
POST: api/register
{
    'first_name': 'xxxx',
    'last_name': 'xxxx',
    'email': 'xxx@xxx,
    'username': 'xxx',
    'password': 'xxxx'
}

POST: api/login
{
    'username': 'xxx',
    'password': 'xxxx'
}

POST: api/logout

GET: api/courses/search?query=searchText [Authenticated]
returns: 
    [
        course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'capacity': x,
            'enrollments_count': x,
            'schedule': 'Sun, Tue, Thu (9:00 - 10:00)',
            'description': 'xxxx',
            'prerequisite_name': 'xxxx'
        }
    ]

POST: api/registered-courses [Authenticated]
[
    'course_code1',
    'course_code2',
    'course_code3'
]

GET: api/registered-courses [Authenticated]
returns: 
    [
        course: {
            'name': 'xxxx',
            'instructor': 'xxxx',
            'days': 'Sunday, Tuesday, Thursday ',
            'time': '9:00 - 10:00',
            'room_no': xx
        }
    ]

GET: api/notifications [Authenticated]
returns: 
    [
        'xxxx',
        'xxxx'
    ]

POST: api/admin/courses [Admin only]
{
    'code': 'xxxx',
    'name': 'xxxx',
    'instructor': 'xxxx',
    'description': 'xxxx'
    'prerequisite_course_code': 'xxxx',
    'capacity': xx,
    'start_time': '9:00',
    'end_time': '9:00',
    'days': 'Sunday, Tuesday, Thursday'
    'room_number': xx,
}

GET: reports and analytics [Authenticated]
```
