from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, sample_product


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='Home'),
    path('contacts/', contacts, name='Contacts'),
    path('sample/', sample_product, name='Products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
