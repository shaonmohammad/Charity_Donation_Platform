
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from events.models import Event_Model

@receiver(post_save, sender=Event_Model)
def send_email_notification(sender, instance, **kwargs):
    subject = 'New Event Alert!!'
    event_title = instance.title
    from_email = 'techtitans531@gmail.com'  

    
    for user in User.objects.all():
        recipient_name = user.username  # You can use user's first_name and last_name fields if available
        recipient_email = user.email
        message = f'Hi {recipient_name},\n\nNew event available: {event_title}'
        try:
            send_mail(subject, message, from_email, [recipient_email])
        except Exception as e:
            print(f"An error occurred while sending email to {recipient_email}: {e}")




