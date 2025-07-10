from django.urls import path, include
from . import  views
from .views import Home, Edit

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('edit/', Edit.as_view(), name='edit'),
]