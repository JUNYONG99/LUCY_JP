from django.shortcuts import get_object_or_404, render
from .models import Category, Faq


def faq(request):
    faq_list = Faq.objects.order_by('-category')
    category = Category.objects.all()
    
    context = {
        'faq_list': faq_list,
        'categories' : category,
        'no_category_faq_count' : Faq.objects.filter(category=None).count(),
        'current_page': 'faq',
        }

    return render(request, "faq/faq_jp.html", context)



