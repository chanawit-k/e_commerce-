from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    product_object = Products.objects.all()

    # search section 
    search_product = request.GET.get('search_product')
    if search_product != '' and search_product is not None:
        product_object = product_object.filter(title__icontains = search_product )

    # paginator section 
    paginator = Paginator(product_object,4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object':product_object})