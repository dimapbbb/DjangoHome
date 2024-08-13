from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'title': "Skystore"
    }
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    context = {
        'title': "Контакты"
    }
    return render(request, 'contacts.html', context)


def sample_product(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,
        "title": "Продукты"
    }
    return render(request, 'sample_product.html', context)
