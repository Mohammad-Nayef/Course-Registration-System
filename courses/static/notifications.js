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
        span.textContent = 'There are no notifications at this time.';

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
});
