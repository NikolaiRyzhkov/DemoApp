import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql_jwt.decorators import login_required
from django.utils import timezone

from .types import UserType
from demoApp.settings import TTL_EMAIL_VERIFICATION_CODE
from .models import EmailVerificationCode

class CreateUser(graphene.Mutation):
    """Create new user"""
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    @staticmethod
    def mutate(self, info, username, password, email):
        user = get_user_model()(username=username,
                                email=email)
        user.set_password(password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class ConfirmationEmail(graphene.Mutation):
    """
    Set True for user.email.verified if the code is correct
    and the validity period has not expired
    """
    info = graphene.String()

    class Arguments:
        code = graphene.Int(required=True)

    @login_required
    def mutate(self, info, code: int):
        user = info.context.user
        email_verification_code = EmailVerificationCode.objects.filter(user=user.id).latest()
        date_code_generation = email_verification_code.date_code_generation
        if user.email_verified:
            info = 'Email has already been confirmed'
        elif date_code_generation + TTL_EMAIL_VERIFICATION_CODE < timezone.now():
            info = 'code is expired'
        elif code == email_verification_code.verification_code:
            user.email_verified = True
            user.save()
            info = 'email_verified'
        else:
            info = 'Incorrect code'
        return ConfirmationEmail(info=info)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    create_user = CreateUser.Field()
    confirmation_email = ConfirmationEmail.Field()
