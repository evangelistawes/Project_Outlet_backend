from rest_framework import routers
from shoes.api.views import ShoesViewSet 
from user.api.views import UserViewSet
from rating.api.views import RatingViewSet
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'shoes', ShoesViewSet)
router.register(r'user', UserViewSet)
router.register(r'rating',RatingViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
