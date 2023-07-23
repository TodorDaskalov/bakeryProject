from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from bakeryProject import settings

UserModel = get_user_model()


def send_mail_successful_registration(user):
    html_message = render_to_string(
        'users/confirmation_email.html',
        {'user': user},
    )

    plain_message = strip_tags(html_message)

    send_mail(
        subject='Registration successful!',
        message='Welcome to my bakery!',
        html_message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email, )
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_mail_successful_registration(instance)
