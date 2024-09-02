from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(TemplateView):
    """
    Просмотр домашней страницы
    """
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        """ Получение контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Skystore"
        return context


class ContactsView(TemplateView):
    """ Просмотр страницы контактов """
    template_name = "catalog/contacts.html"

    def post(self, request, **kwargs):
        """ Обработка POST запроса"""
        context = self.get_context_data(**kwargs)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """ Получение данных контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context


class ProductListView(ListView):
    """
    Просмотр страницы продуктов
    """
    model = Product

    def get_context_data(self, **kwargs):
        """ Получение данных контекста"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Продукты"
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
