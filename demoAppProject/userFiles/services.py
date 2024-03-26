from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from graphql import GraphQLResolveInfo

from .models import TxtFile


def create_txt_file(info: GraphQLResolveInfo, file: InMemoryUploadedFile) -> TxtFile:
    """create the .txt file, model: UserTxt"""
    txt_file = TxtFile.objects.create(
        owner=info.context.user,
        file=ContentFile(content=file.file.read(), name=file.name),
    )
    return txt_file


def get_number_of_lines_in_file(path: str) -> int:
    """return number of lines"""
    with open(path, 'r') as file:
        count = 0
        for line in file:
            count += 1
        return count
