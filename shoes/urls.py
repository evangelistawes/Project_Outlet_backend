from django.urls import path
from. import views

urlpatterns =[
    path("", views.index, name = "index"),
    path("<int:shoes_id>/detail/", views.detail, name = "detail"),
]