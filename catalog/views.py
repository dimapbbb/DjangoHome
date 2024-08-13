from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'contacts.html')


def sample_product(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list
    }
    return render(request, 'sample_product.html', context)
