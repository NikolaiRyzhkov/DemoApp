from graphene_django import DjangoObjectType
from .models import TxtFile, TxtFileInfo


class TxtFileType(DjangoObjectType):
    class Meta:
        model = TxtFile
        exclude = ('txtfileinfo_set',)


class TxtFileInfoType(DjangoObjectType):
    class Meta:
        model = TxtFileInfo
        fields = "__all__"
