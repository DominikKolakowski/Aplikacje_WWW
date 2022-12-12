from rest_framework import generics, permissions
from .serializers import *

User = get_user_model()


# endpoint: wyswietlenie listy uzytkownikow

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'lista-uzytkownikow'


# endpoint: wyswietlenie, edycja, usuniecie uzytkownika

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'detale-uzytkownika'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
