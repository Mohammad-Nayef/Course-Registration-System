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

document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleSidebar = document.getElementById('toggleSidebar');
    const hideSidebar = document.getElementById('hideSidebar');

    toggleSidebar.addEventListener('click', () => {
        sidebar.classList.toggle('show');
        mainContent.classList.toggle('collapsed');
    });

    hideSidebar.addEventListener('click', () => {
        sidebar.classList.remove('show');
        mainContent.classList.remove('collapsed');
    });

        

    fetch('api/user/name', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('short-name').innerHTML = data;
    });

    document.getElementById('logout').addEventListener('click', function(event) {
        const csrfToken = getCookie('csrftoken');

        fetch('/api/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken 
            }
        })            
        .then(response => {
            window.location.href = '/';
        })
    });
})


