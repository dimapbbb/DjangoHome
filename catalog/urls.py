from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView,
                           HomeView,
                           ContactsView,
                           ProductCreateView,
                           ProductDetailView,
                           ProductUpdateView,
                           ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('list/', ProductListView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
