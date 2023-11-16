from django.urls import path, include
from demo import views

urlpatterns = [
    path('', views.index, name='homepage'),
]