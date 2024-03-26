from django.contrib import admin

from .models import CustomUser, EmailVerificationCode


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'email', 'email_verified']


@admin.register(EmailVerificationCode)
class EmailVerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'verification_code', 'date_code_generation']