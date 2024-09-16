from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


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


class ProductListView(LoginRequiredMixin, ListView):
    """
    Просмотр страницы продуктов
    """
    model = Product
    login_url = "/users"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        """ Получение данных контекста"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Продукты"
        for product in self.object_list:
            version = Version.objects.get(product=product.pk, current=True).number
            if version:
                product.version = version
            else:
                product.version = "null"
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context["formset"] = VersionFormset(self.request.POST)
        else:
            context["formset"] = VersionFormset()
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.user = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('pk')
        version = Version.objects.get(product=product_id, current=True)
        context["title"] = Product.objects.get(id=product_id).name
        if version:
            context["version"] = version
        else:
            context["version"] = "null"
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if user.groups.filter(name="moderators").exists():
            obj.prems = True
        else:
            obj.prems = False
        return obj


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return ProductForm
        if user.groups.filter(name="moderators").exists():
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
