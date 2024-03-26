import graphene
from graphql_jwt.decorators import login_required

from .service import gat_and_save_email_verification_code
from .tasks import send_verify_code


class Query(graphene.ObjectType):
    email_verification_code = graphene.String()


    @login_required
    def resolve_email_verification_code(self, info):
        """Creating and sending a code to confirm the user's email"""
        user = info.context.user
        if not user.email:
            return 'The user does not have an email'
        if user.email_verified:
            return 'Email has already been confirmed'
        code = gat_and_save_email_verification_code(user_id=user.id)
        send_verify_code.delay(code=code, email=user.email)
        return True
