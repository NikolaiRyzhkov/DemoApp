from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    """Type for standard django user"""
    class Meta:
        model = get_user_model()
        fields = ('username',)