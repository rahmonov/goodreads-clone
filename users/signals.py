from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Welcome to Goodreads Clone",
            f"Hi, {instance.username}. Welcome to Goodreads Clone. Enjoy the books and reviews.",
            "jrahmonov2@gmail.com",
            [instance.email]
        )
