document.addEventListener('DOMContentLoaded', () => {
    function getCookie(name) {
        const cookies = document.cookie.split('; ');
        for (const cookie of cookies) {
            const [key, value] = cookie.split('=');
            if (key === name) {
                return value;
            }
        }
        return null;
    }

    document.getElementById('add-course').addEventListener('click', async function(event) {
        const courseCode = document.getElementById('courseCode').value;
        const courseName = document.getElementById('courseName').value;
        const courseInstructor = document.getElementById('courseInstructor').value;
        const courseDescription = document.getElementById('courseDescription').value;
        const prerequisiteCode = document.getElementById('prerequisiteCode').value;
        const capacity = document.getElementById('capacity1').value;
        const startTime = document.getElementById('startTime').value;
        const endTime = document.getElementById('endTime').value;
        const roomNumber = document.getElementById('room').value;
        const csrfToken = getCookie('csrftoken');

        const days = [];
        if (document.querySelector('input[name="sunCheckBox"]').checked) days.push('Sunday');
        if (document.querySelector('input[name="monCheckBox"]').checked) days.push('Monday');
        if (document.querySelector('input[name="tueCheckBox"]').checked) days.push('Tuesday');
        if (document.querySelector('input[name="wedCheckBox"]').checked) days.push('Wednesday');
        if (document.querySelector('input[name="thuCheckBox"]').checked) days.push('Thursday');
        if (document.querySelector('input[name="friCheckBox"]').checked) days.push('Friday');
        if (document.querySelector('input[name="satCheckBox"]').checked) days.push('Saturday');

        const data = {
            code: courseCode,
            name: courseName,
            instructor: courseInstructor,
            description: courseDescription,
            prerequisite_course_code: prerequisiteCode,
            capacity: parseInt(capacity),
            start_time: startTime,
            end_time: endTime,
            days: days.join(', '),
            room_number: roomNumber
        };

        const response = await fetch('api/admin/courses', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken 
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                return response.text();
            }
            alert('Course registered successfully.')
        })
        .then(error => {
            if (error)
                alert(error)
        })
        .catch(error => {
            alert('Error: ' + error.message);
        });
    });
})