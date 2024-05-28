document.addEventListener('DOMContentLoaded', () => {
    var courseCard = document.querySelectorAll('.course-left');

    for (var i = 0; i < courseCard.length; i++) {
        courseCard[i].addEventListener('click', function() {
            var childrenArray = Array.from(this.children);
            if (this.style.height === '25vh') {
                childrenArray[2].style.display = 'none';
                this.style.height = 'auto';
                return;
            } else {
                this.style.height = '25vh';
                childrenArray[2].style.display = 'block';
            }
        });
    }

    document.getElementById('search-button').addEventListener('click', function() {
        var searchText = document.getElementById('search-placeholder').value;

        if (searchText.trim() !== '') {
            fetch('api/courses?query=' + searchText)
                .then(response => response.json())
                .then(data => {
                    printCourses(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
        console.log(data);
    });

    function printCourses(data) {
        const form = document.getElementById('search-result');

        data.forEach(course => {
            let courseElement = document.createElement('div');
            courseElement.className = 'course';

            let courseHTML = `
                <div class="course-left">
                    <span class="course-name">${course.name}<span style="margin-left: 6px;">${course.code}</span></span>
                    <div>
                        <span class="course-instrutor-name">${course.instructor}</span>
                        <span class="course-hours">${course.schedule}</span>
                        <span class="course-room">Room 101</span><br>
                    </div>
                    <div class="course-description">
                        <span class="prerequisite-Code">Prerequisite Course : ${course.prerequisite_name}</span><br>
                        <span>Course Description: ${course.description}</span>
                    </div>
                </div>
                <div class="course-right">
                    <span class="course-enrollment ${course.enrollments_count >= course.capacity ? 'text-danger' : ''}">
                        <span>${course.enrollments_count}</span>/<span>${course.capacity}</span>
                    </span>
                    <input type="checkbox" class="course-check" ${course.enrollments_count >= course.capacity ? 'disabled="disabled"' : ''}>
                </div>
            `;

            courseElement.innerHTML = courseHTML;
            form.appendChild(courseElement);
        });
    }

    const form = document.getElementById('search-result');

    data.forEach(course => {
        let courseElement = document.createElement('div');
        courseElement.className = 'course';

        let courseHTML = `
            <div class="course-left">
                <span class="course-name">${course.name}<span style="margin-left: 6px;">${course.code}</span></span>
                <div>
                    <span class="course-instrutor-name">${course.instructor}</span>
                    <span class="course-hours">${course.schedule}</span>
                    <span class="course-room">Room 101</span><br>
                </div>
                <div class="course-description">
                    <span class="prerequisite-Code">Prerequisite Course : ${course.prerequisite_name}</span><br>
                    <span>Course Description: ${course.description}</span>
                </div>
            </div>
            <div class="course-right">
                <span class="course-enrollment ${course.enrollments_count >= course.capacity ? 'text-danger' : ''}">
                    <span>${course.enrollments_count}</span>/<span>${course.capacity}</span>
                </span>
                <input type="checkbox" class="course-check" value="${course.code}" ${course.enrollments_count >= course.capacity ? 'disabled="disabled"' : ''}>
            </div>
        `;

        courseElement.innerHTML = courseHTML;
        form.appendChild(courseElement);
    });

    document.getElementById('add-courses').addEventListener('click', function(event) {
        event.preventDefault();
        
        const selectedCourses = Array.from(document.querySelectorAll('.course-check:checked'))
                                     .map(checkbox => checkbox.value);

        if (selectedCourses.length > 0) {
            fetch('api/registered-courses', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(selectedCourses)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('Courses successfully added!');
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('An error occurred while adding courses.');
            });
        } else {
            alert('No courses selected.');
        }
    });
})