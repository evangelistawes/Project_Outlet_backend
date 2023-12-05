from user.models import User
from user.api.serializer import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False) 
    def create_user(self, request):
        username = request.data.get('username')
        if username is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        User.objects.create(username=username)
        return Response(status=status.HTTP_201_CREATED)
