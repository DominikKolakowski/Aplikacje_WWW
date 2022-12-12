from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from accounts.models import UserAccount



#-----------Endpointy dla Producentów -----------------------

# endpoint: wypisanie listy producentow
class ProducentList(generics.ListAPIView):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer
    name = 'lista-producentow'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: tworzenie  producenta
class CreateProducent(generics.CreateAPIView):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer
    name = 'tworzenie-producenta'

    def perform_create(self, serializer):
        serializer.save()

# endpoint: usuwanie producenta
class ProducentDelete(generics.DestroyAPIView):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer
    name = 'usuwanie-producenta'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# endpoint: edytowanie producenta
class ProducentEdit(generics.UpdateAPIView):
    queryset = Producent.objects.all()
    serializer_class = ProducentSerializer
    name = 'edytowanie-producenta'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# endpoint: szukanie produktów po producentach ID
class Producent_szukaj(ListAPIView):
    serializer_class = ProduktySerializer
    lookup_field = 'producent'
    def get_queryset(self):
        producent = self.kwargs['producent']
        return Produkty.objects.filter(producent=producent)




# -----------Endpointy dla Kategorii -----------------------

# endpoint: wypisanie listy kategori
class KategoriaList(generics.ListAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'lista-kategorii'

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

# endpoint: tworzenie  producenta
class CreateKategoria(generics.CreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'tworzenie-kategorii'

    def perform_create(self, serializer):
        serializer.save()

# endpoint: usuwanie kategorii
class KategoriaDelete(generics.DestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'usuwanie-kategorii'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: edytowanie kategorii
class KategoriaEdit(generics.UpdateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'edytowanie-kategorii'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# endpoint: szukanie produktów po kategoriach ID
class Kategoria_szukaj(ListAPIView):
    serializer_class = ProduktySerializer
    lookup_field = 'kategoria'
    def get_queryset(self):
        kategoria = self.kwargs['kategoria']
        return Produkty.objects.filter(kategoria=kategoria)





# -----------Endpointy dla Produktów -----------------------

# endpoint: wypisanie listy produktow
class ProduktytList(generics.ListAPIView):
        queryset = Produkty.objects.all()
        serializer_class = ProduktySerializer
        name = 'lista-produktow'

        if (UserAccount.is_staff == True):
            def perform_create(self, serializer):
                serializer.save(user=self.request.user)



# endpoint: tworzenie nowego produktu
class CreateProdukt(generics.CreateAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'tworzenie-produktu'

    def perform_create(self, serializer):
        serializer.save()

# endpoint: usuwanie produktu
class ProduktDelete(generics.DestroyAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'usuwanie-produktu'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: edytowanie produktu
class ProduktEdit(generics.UpdateAPIView):
    queryset = Produkty.objects.all()
    serializer_class = ProduktySerializer
    name = 'edytowanie-produktu'


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# endpoint: kupienie produktu
class KupProdukt(APIView):
    def put(self, pk):
        produkt = Produkty.objects.get(id=pk)
        if (produkt.ilosc <= 0):
            return Response('Brak produktu na magazynie')
        else:
            produkt.ilosc -= 1
            produkt.save()
            return Response('Kupiłeś produkt')
