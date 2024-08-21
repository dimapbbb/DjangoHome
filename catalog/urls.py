from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, HomeView, ContactsView


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('contacts/', ContactsView.as_view(), name='Contacts'),
    path('sample/', ProductListView.as_view(), name='Products'),
]
