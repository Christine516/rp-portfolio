from django.urls import path
from hello_world import views

urlpatterns = [
    path('home/', views.hello_world, name='hello_world'),
]
