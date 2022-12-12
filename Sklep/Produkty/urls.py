from django.urls import path
from . import views


urlpatterns = [
    #endpointy dla producentow
    path('producenci', views.ProducentList.as_view(), name='lista-producentow'),
    path('producenci/add', views.CreateProducent.as_view(), name='tworzenie-producenta'),
    path('producenci/delete/<int:pk>', views.ProducentDelete.as_view(), name='usuwanie-producenta'),
    path('producenci/edit/<int:pk>', views.ProducentEdit.as_view(), name='edytowanie-producenta'),
    path('producenci/szukaj/<int:producent>', views.Producent_szukaj.as_view(), name='szukaj-producenta-po-id'),

    #endpointy dla kategorii
    path('kategoria', views.KategoriaList.as_view(), name='lista-kategorii'),
    path('kategoria/add', views.CreateKategoria.as_view(), name='tworzenie-kategorii'),
    path('kategoria/delete/<int:pk>', views.KategoriaDelete.as_view(), name='usuwanie-kategorii'),
    path('kategoria/edit/<int:pk>', views.KategoriaEdit.as_view(), name='edytowanie-kategorii'),
    path('kategoria/szukaj/<int:kategoria>', views.Kategoria_szukaj.as_view(), name='szukaj-kategori-po-id'),

    #endpointy dla produktow
    path('produkty', views.ProduktytList.as_view(), name='lista-produktow'),
    path('produkty/add', views.CreateProdukt.as_view(), name='tworzenie-produktu'),
    path('produkty/delete/<int:pk>', views.ProduktDelete.as_view(), name='usuwanie-produktu'),
    path('produkty/edit/<int:pk>', views.ProduktEdit.as_view(), name='edytowanie-produktu'),
    path('produkty/kup/<int:pk>', views.KupProdukt.as_view(), name='% kup-produkt %'),

]