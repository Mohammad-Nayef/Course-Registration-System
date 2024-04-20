# System APIs
```http
POST: api/register
{
    'first_name': 'xxxx',
    'last_name': 'xxxx',
    'email': 'xxx@xxx',
    'password': 'xxxx'
}

POST: api/login
{
    'email': 'xxx@xxx',
    'password': 'xxxx'
}

GET: api/search?text=searchText
returns: 
    [
        course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'capacity': x,
            'enrollments': x,
            'schedule': 'Sun, Tue, Thu (9:00 - 10:00)',
            'description': 'xxxx',
            'prerequisites': 'xxxx'
        }
    ]

GET: api/courses/<course-code>
returns:
    course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'capacity': x,
            'enrollments': x,
            'schedule': 'Sun, Tue, Thu (9:00 - 10:00)',
            'description': 'xxxx',
            'prerequisites': 'xxxx'
    }

POST: api/registered-courses
{
    'course_code': 'xxxx'
}

GET: api/registered-courses
returns: 
    [
        course: {
            'name': 'xxxx',
            'code': 'xxxx',
            'instructor': 'xxxx',
            'days': 'Sun, Tue, Thu',
            'time': '1111 - 1111',
        }
    ]

GET: api/notifications
returns: 
    [
        {
            'content': 'xxxx',
            'date_time': 'xxxx'
        }
    ]

GET: reports and analytics 
```
