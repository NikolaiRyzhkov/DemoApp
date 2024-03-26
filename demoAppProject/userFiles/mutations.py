import graphene
from django.core.files.uploadedfile import InMemoryUploadedFile
from graphene_file_upload.scalars import Upload
from graphql import GraphQLResolveInfo
from graphql_jwt.decorators import login_required

from .services import create_txt_file
from demoApp.custom_permissions import email_verified
from .types import TxtFileType
from .tasks import create_txt_file_info

class UploadTxtFile(graphene.Mutation):
    """Upload and save the user .txt file"""

    class Arguments:
        file = Upload(required=True)

    txt_file = graphene.Field(TxtFileType)

    @login_required
    @email_verified
    def mutate(self, info: GraphQLResolveInfo, file: InMemoryUploadedFile):
        txt_file = create_txt_file(info=info, file=file)
        create_txt_file_info.delay(txt_file_id=txt_file.id, owner_id=info.context.user.id)
        return UploadTxtFile(txt_file=txt_file)


class Mutation(graphene.ObjectType):
    upload_txt_file = UploadTxtFile.Field()
