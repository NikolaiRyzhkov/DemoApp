import graphene
from graphql_jwt.decorators import login_required
from django.core.cache import cache

from .types import TxtFileType, TxtFileInfoType
from .models import TxtFile, TxtFileInfo
from demoApp.custom_permissions import email_verified


class Query(graphene.ObjectType):
    txt_file = graphene.Field(TxtFileType, id_txt_file=graphene.Int())
    txt_file_info = graphene.Field(TxtFileInfoType, id_txt_file=graphene.Int())
    txt_file_list = graphene.List(TxtFileType)

    @login_required
    @email_verified
    def resolve_txt_file(self, info, id_txt_file=None):
        """return a TxtFile by id, or last created"""
        if id_txt_file:
            txt_file = TxtFile.objects.get(id=id_txt_file, owner=info.context.user)
        else:
            txt_file = TxtFile.objects.filter(owner=info.context.user).latest('created_at')
        return txt_file

    @login_required
    @email_verified
    def resolve_txt_file_info(self, info, id_txt_file=None):
        """return a TxtFileInfo by id TxtFile, or last created for current user"""
        user = info.context.user
        file_cache = cache.get(f'txt_file_info_latest_{user.id}')

        if file_cache:
            if id_txt_file is None or file_cache.txt_file.id == id_txt_file:
                return file_cache
        else:
            txt_file_info_all = TxtFileInfo.objects.select_related('txt_file').select_related('txt_file__owner')
            user_txt_file_info = txt_file_info_all.filter(txt_file__owner=user)
            if id_txt_file is None:
                return user_txt_file_info.latest('txt_file__created_at')
            else:
                return user_txt_file_info.get(id=id_txt_file)

    @login_required
    @email_verified
    def resolve_txt_file_list(self, info):
        """return all txt file of a current user"""
        user = info.context.user
        all_user_txt_file = TxtFile.objects.filter(owner=user)
        return all_user_txt_file

