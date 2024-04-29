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
returns: {
    'token': 'xxxx'
}

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

GET: api/courses/<course-code> [Authenticated]
returns:
    course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'capacity': x,
            'enrollments_count': x,
            'schedule': 'Sunday, Tuesday, Thursday (9:00 - 10:00)',
            'description': 'xxxx',
            'prerequisite_name': 'xxxx'
    }

POST: api/registered-courses [Authenticated]
{
    'course_code': 'xxxx'
}

GET: api/registered-courses [Authenticated]
returns: 
    [
        course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'schedule': 'Sunday, Tuesday, Thursday (9:00 - 10:00)'
        }
    ]

GET: api/notifications [Authenticated]
returns: 
    [
        {
            'content': 'xxxx',
            'date_time': 'xxxx'
        }
    ]

GET: reports and analytics [Authenticated]
```
