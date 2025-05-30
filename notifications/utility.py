from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

def create_notification(user, title, message, notification_type='info', url=None):
    """
    Create a new notification for a user
    """
    notification = Notification.objects.create(
        user=user,
        title=title,
        message=message,
        notification_type=notification_type,
        url=url
    )
    
    # In a real implementation, you would send a WebSocket message here
    # to notify the user in real-time
    
    return notification

def send_notification_to_all_users(title, message, notification_type='info', url=None):
    """
    Send a notification to all users
    """
    users = User.objects.all()
    for user in users:
        create_notification(user, title, message, notification_type, url)

def send_notification_to_group(users, title, message, notification_type='info', url=None):
    """
    Send a notification to a group of users
    """
    for user in users:
        create_notification(user, title, message, notification_type, url)