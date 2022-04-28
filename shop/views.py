from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    product_object = Products.objects.all()

    search_product = request.GET.get('search_product')
    if search_product != '' and search_product is not None:
        product_object = product_object.filter(title__icontains = search_product )

    return render(request, 'shop/index.html', {'product_object':product_object})