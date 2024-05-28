document.addEventListener('DOMContentLoaded', () => {
    fetch('api/admin/reports')
    .then(response => response.json())
    .then(data => {
        document.getElementById('number-of-courses').innerText = data.number_of_courses;
        document.getElementById('number-of-students').innerText = data.number_of_students;
        document.getElementById('number-of-enrollments').innerText = data.number_of_enrollments;
    })
    .catch(error => console.error('Error fetching data:', error));

    fetch('api/admin/courses?order-by=popularity')
    .then(response => response.json())
    .then(data => {
        const codeContainer = document.getElementById('code');
        const nameContainer = document.getElementById('name');
        const registeredContainer = document.getElementById('registered');
        const capacityContainer = document.getElementById('capacity');

        data.forEach(course => {
            codeContainer.innerHTML += `<div class="row details-statistics">${course.code}</div>`;
            nameContainer.innerHTML += `<div class="row details-statistics">${course.name}</div>`;
            registeredContainer.innerHTML += `<div class="row details-statistics mx-5">${course.enrollments_count}</div>`;
            capacityContainer.innerHTML += `<div class="row details-statistics mx-5">${course.capacity}</div>`;
        });
    })
    .catch(error => console.error('Error fetching data:', error));
})