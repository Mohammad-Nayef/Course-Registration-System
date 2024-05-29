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

    
    function openDetails() {
        var courseCard = document.querySelectorAll('.course-left');

        for (var i = 0; i < courseCard.length; i++) {
            courseCard[i].addEventListener('click', function() {
                var childrenArray = Array.from(this.children);
                if (!this.dataset.originalHeight) {
                    this.dataset.originalHeight = this.clientHeight + 'px';
                }
                if (this.style.height === 'auto') {
                    childrenArray[2].style.display = 'none';
                    this.style.height = this.dataset.originalHeight;
                } else {
                    childrenArray[2].style.display = 'block';
                    this.style.height = 'auto';
                }
            });
        }
    }

    let result=[];

    
    function showResult() {
        var searchText = document.getElementById('search-placeholder').value;

        if (searchText.trim() !== '') {
            fetch('api/courses?query=' + searchText)
                .then(response => response.json())
                .then(data => {
                    result = data;
                    printCourses(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }

    document.getElementById('search-button').addEventListener('click', showResult);


    function printCourses(data) {
        let form = document.getElementById('search-result');

        while (form.firstChild) {
            form.removeChild(form.firstChild);
        }

        data.forEach(course => {
            let disabled = '', red = '';
            if (course.enrollments_count >= course.capacity) {
                disabled = 'disabled="disabled"';
                red = 'text-danger';
            } else if (course.is_registered) {
                disabled = 'disabled="disabled"';
            }

            let content = `
                <div class="course">
                    <div class="course-left">
                        <span class="course-name"><span style="margin-left: 6px;" id="code">${course.code}</span> ${course.name}</span>
                        <div>
                            <span class="course-instrutor-name">${course.instructor}</span>
                            <span class="course-hours"> | ${course.schedule}</span>
                        </div>
                        <div class="course-description">
                            <span class="prerequisite-Code">Prerequisite Course : ${course.prerequisite_name}</span><br>
                            <span>Course Description: ${course.description}.</span>
                        </div>
                    </div>
                    <div class="course-right">
                        <span class="course-enrollment ${red}"><span>${course.enrollments_count}</span>/<span>${course.capacity}</span></span>
                        <input type="checkbox" id="${course.code}" class="course-check" ${disabled}></div>
                </div>
            `;
            const tempContainer = document.createElement("div");
            tempContainer.innerHTML = content;
            form.appendChild(tempContainer);  
        });
        openDetails();          
    }


    document.getElementById('add-courses').addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('.course-check');
        const checkedCourses = [];
        
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                checkedCourses.push(checkbox.id);
            }
        });

        if (checkedCourses.length > 0) {
            const csrfToken = getCookie('csrftoken');
            const requestBody = JSON.stringify(checkedCourses);
            
            fetch('api/registered-courses', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken 
                },
                body: requestBody
            })
            .then(response => {
                if (response.ok) {
                    showResult();
                    alert('Courses successfully registered');
                } else {
                    return response.json();
                }
            })
            .then(errorMessage => {
                if (errorMessage)
                    alert(errorMessage)
            })
            .catch(error => {
                alert('Error registering courses:', error);
            });
        }
    });
})