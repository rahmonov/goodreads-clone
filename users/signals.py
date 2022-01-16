from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser
from users.tasks import send_email


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_email.delay(
            "Welcome to Goodreads Clone",
            f"Hi, {instance.username}. Welcome to Goodreads Clone. Enjoy the books and reviews.",
            [instance.email]
        )
