from django.core.mail import send_mail
from random import randint

from .models import EmailVerificationCode, CustomUser


def gat_and_save_email_verification_code(user_id: int) -> int:
    """create and save random email verification code"""
    code = randint(100000, 1000000)
    email_verification_code = EmailVerificationCode()
    email_verification_code.user = CustomUser.objects.get(id=user_id)
    email_verification_code.verification_code = code
    email_verification_code.save()
    return code
