import graphene
from graphene_django import DjangoObjectType
from .models import Cars


class CarsType(DjangoObjectType):
    class Meta:
        model = Cars
        fields = ("id","mark", "model", "year")

class Query(graphene.ObjectType):

    all_cars = graphene.List(CarsType)

    def resolve_all_cars(root, info):
        return Cars.objects.all()

schema = graphene.Schema(query = Query)