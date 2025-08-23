from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Надсилає тестовий email для перевірки налаштувань SMTP"

    def handle(self, *args, **options):
        subject = "Тестовий лист із Django"
        message = "Якщо ви бачите цей лист, то налаштування email працюють"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        try:
            send_mail(subject, message, from_email, recipient_list)
            self.stdout.write(self.style.SUCCESS(f"Лист успішно надіслано на {recipient_list}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Помилка: {e}"))
