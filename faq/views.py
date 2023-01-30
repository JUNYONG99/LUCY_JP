from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Category, Faq, CategoryJP, FaqJP


def faq(request):
    faq_list = Faq.objects.order_by('-category')
    category = Category.objects.all()
    
    #넘겨줄 값
    context = {
        'faq_list': faq_list,
        'categories' : category,
        'no_category_faq_count' : Faq.objects.filter(category=None).count(),
        'current_page': 'faq',
        }

    return render(request, "faq/faq.html", context)


def faqJP(request):
    faq_list = FaqJP.objects.order_by('-category')
    category = CategoryJP.objects.all()
    
    #넘겨줄 값
    context = {
        'faq_list': faq_list,
        'categories' : category,
        'no_category_faq_count' : FaqJP.objects.filter(category=None).count(),
        'current_page': 'faq',
        }

    return render(request, "faq/faq_jp.html", context)

