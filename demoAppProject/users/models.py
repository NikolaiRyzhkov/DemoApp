from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class EmailVerificationCode(models.Model):
    """Model for storing email verification code"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verification_code = models.IntegerField()
    date_code_generation = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'date_code_generation'
