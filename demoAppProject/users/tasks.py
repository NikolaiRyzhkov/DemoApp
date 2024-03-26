from demoApp.celery import app

from django.core.mail import send_mail


@app.task()
def send_verify_code(code: int, email: str) -> None:
    """send a cod for verification user email"""
    send_mail(
        subject='The cod for verification user email',
        message='Cod: {0}'.format(str(code)),
        recipient_list=[email],
        from_email=None
    )
