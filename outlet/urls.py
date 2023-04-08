from rest_framework import routers
from shoes.api.views import ShoesViewSet 
from user.api.views import UserViewSet
from rating.api.views import RatingViewSet
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'shoes', ShoesViewSet)
router.register(r'user', UserViewSet)
router.register(r'rating',RatingViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
]
