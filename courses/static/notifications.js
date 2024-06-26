

function fetchUserName() {
    return fetch('api/user/name')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        });
}

function updateGreeting(userName) {
    const userNameElement = document.getElementById('user-name');
    const shortNameElement = document.getElementById('short-name');
    userName = userName.slice(1, -1); // to remove " " around the name
    userNameElement.textContent = userName;
    shortNameElement.textContent = userName.split(' ')[0];
}

function fetchNotifications() {
    return fetch('api/notifications')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        });
}

function displayNotifications(notifications) {
    const notificationsContainer = document.getElementById('notifications');
    notificationsContainer.innerHTML = '';

    if (notifications.length === 0) {
        const noNotificationsMessage = document.createElement('div');
        noNotificationsMessage.classList.add('no-notifications-message');
        
        const span = document.createElement('span');
        span.textContent = 'There are no notifications';

        noNotificationsMessage.appendChild(span);
        notificationsContainer.appendChild(noNotificationsMessage);
    } else {
        notifications.forEach(notificationText => {
            const notificationContent = document.createElement('div');
            notificationContent.classList.add('notification-card');

            const span = document.createElement('span');
            span.textContent = notificationText;

            notificationContent.appendChild(span);
            notificationsContainer.appendChild(notificationContent);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchNotifications()
        .then(notifications => displayNotifications(notifications))
        .catch(error => console.error('Error fetching notifications:', error));
    fetchUserName()
        .then(userName => {
            updateGreeting(userName);
        })
        .catch(error => console.error('Error fetching user name:', error));
});