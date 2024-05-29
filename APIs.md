# System APIs
### Register a user:
```http
POST: api/register
{
    'first_name': 'xxxx',
    'last_name': 'xxxx',
    'email': 'xxx@xxx,
    'username': 'xxx',
    'password': 'xxxx'
}
```
### Login a user:
```http
POST: api/login
{
    'username': 'xxx',
    'password': 'xxxx'
}
```
### Logout a user:
```http
POST: api/logout
```
### Search courses:
```http
GET: api/courses?query=searchText [Authenticated]
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
            'prerequisite_name': 'xxxx',
            'is_registered': bool
        }
    ]
```
### Register courses:
```http
POST: api/registered-courses [Authenticated]
[
    'course_code1',
    'course_code2',
    'course_code3'
]
```
### Get a list all the registered courses:
```http
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
```
### Get a list of notifications:
```http
GET: api/notifications [Authenticated]
returns: 
    [
        'xxxx',
        'xxxx'
    ]
```
### Create a course:
```http
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
```
### Get the courses for admin ordered by popularity:
```http
GET: api/admin/courses?order-by=popularity [Admin only]
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
```
### Get reports and analytics:
```http
GET: api/admin/reports [Admin only]
returns: {
    'number_of_students': xx,
    'number_of_courses': xx,
    'number_of_enrollments': xx
}
```
### Get name of the user
```http
GET: api/user/name
returns: {
    'user name'
}
```