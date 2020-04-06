from django.urls import path
from art_gallery import views

urlpatterns = [
    path('art/', views.art_gallery, name='art_gallery'),
]
