document.addEventListener('DOMContentLoaded', () => {
    fetch('api/admin/reports')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const coursesElement = document.getElementById('number-of-courses');
            const studentsElement = document.getElementById('number-of-students');
            const enrollmentsElement = document.getElementById('number-of-enrollments');

            if (coursesElement) coursesElement.innerText = data.number_of_courses;
            if (studentsElement) studentsElement.innerText = data.number_of_students;
            if (enrollmentsElement) enrollmentsElement.innerText = data.number_of_enrollments;
        })
        .catch(error => console.error('Error fetching reports data:', error));

    fetch('api/admin/courses?order-by=popularity')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const codeContainer = document.getElementById('course-code');
            const nameContainer = document.getElementById('course-name');
            const registeredContainer = document.getElementById('registered');
            const capacityContainer = document.getElementById('capacity');

            codeContainer.innerHTML = '<div class="row table-header">Code</div>';
            nameContainer.innerHTML = '<div class="row table-header">Name</div>';
            registeredContainer.innerHTML = '<div class="row table-header">Registered</div>';
            capacityContainer.innerHTML = '<div class="row table-header">Capacity</div>';

            data.forEach(course => {
                codeContainer.innerHTML += `<div class="row details-statistics">${course.code}</div>`;
                nameContainer.innerHTML += `<div class="row details-statistics">${course.name}</div>`;
                registeredContainer.innerHTML += `<div class="row details-statistics mx-5">${course.enrollments_count}</div>`;
                capacityContainer.innerHTML += `<div class="row details-statistics mx-5">${course.capacity}</div>`;
            });
        })
        .catch(error => console.error('Error fetching courses data:', error));
});
