from shoes.models import Shoes
from shoes.api.serializer import ShoesSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('gender','price')

    @action(methods=['POST'], detail=False)
    def create_shoes(self,request):
        if request.data.get('shoes_name') is None:
            return Response({
                "Failed":"Forneca o modelo"
            })
        if request.data.get('brand') is None:
            return Response({
                "Failed":"Forneca a marca"})
        if request.data.get('gender') is None:
            return Response({
                "failed": "Forneca o Genero"
            })
        Shoes.objects.create(shoes_name=request.data.get('shoes_name'),
                             brand=request.data.get('brand'), 
                             gender=request.data.get('gender'))
        return Response(status=status.HTTP_201_CREATED)