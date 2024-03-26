import graphene

from users.mutations import Mutation as UsersMutation
from users.query import Query as UsersQuery
from userFiles.mutations import Mutation as UserFilesMutation
from userFiles.query import Query as QueryUserFiles


class Query(UsersQuery, QueryUserFiles):
    """Combine the queries form different apps"""
    pass


class Mutation(UsersMutation, UserFilesMutation):
    """Combine the mutations from different apps"""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
