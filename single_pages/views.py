from django.shortcuts import render
from shop.models import Brand, Product

def landing(request):
    product_list = Product.objects.order_by('-like_count')[:4]
    arrival_list = Product.objects.order_by('-created_at')[:4]
    context = {
        'product_list': product_list,
        'arrival_list': arrival_list,
        'brand_list': Brand.objects.order_by('?')[:4],
        'current_page': 'landing',
    }
    return render(request, "single_pages/landing_jp.html", context)

def about(request):
    return render(
        request,
        'single_pages/about_jp.html',
        {
            'current_page': 'about',
        }
    )


