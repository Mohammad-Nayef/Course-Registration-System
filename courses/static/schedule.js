document.addEventListener("DOMContentLoaded", function () {
    fetch('api/registered-courses', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(course => {
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <th scope="row">${course.name}
                    <br><span class="instructor-name">${course.instructor}</span>
                    <br><span class="room">${course.room_no}</span>
                </th>
            `;

            const daysOfWeek = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
            daysOfWeek.forEach(day => {
                const cell = document.createElement('td');
                if (course.days.includes(day)) {
                    cell.textContent = course.time;
                }
                newRow.appendChild(cell);
            });

            document.getElementById('schedule-body').appendChild(newRow);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});