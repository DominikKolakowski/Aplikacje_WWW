from django.urls import path
from . import views


urlpatterns = [
    # endpointy dla usera
    path('users', views.UserList.as_view(), name='lista-uzytkownikow'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='detale-uzytkownika'),
]