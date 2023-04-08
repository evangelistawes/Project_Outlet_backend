from rest_framework import viewsets, status
from rating.api.serializer import RatingSerializer
from rating.models import Rating
from user.models import User
from shoes.models import Shoes
from rest_framework.decorators import action
from rest_framework.response import Response

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


    @action(methods=['POST'], detail=False)
    def create_rating(self, request):
        try:
            Rating.objects.create(
                title=request.data.get('title'),
                content = request.data.get('content'),
                grade = request.data.get('grade'),
                author = User.objects.get(id=request.data.get('author')),
                shoes_avaliated = Shoes.objects.get(id= request.data.get('shoes'))
            )
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)