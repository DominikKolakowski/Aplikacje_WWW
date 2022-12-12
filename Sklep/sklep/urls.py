from django.urls import path, include, re_path
from  django.views.generic import TemplateView
from django.contrib import  admin

urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('produkty/',include('Produkty.urls')),

]

urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]