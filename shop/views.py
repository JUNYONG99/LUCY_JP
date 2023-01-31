import json
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.core import serializers
from django.contrib import messages
from account.models import User
from .models import Inquiry, Product, Category, Brand, Like, Cart, Review
from .forms import ReviewForm, InquiryForm


def shop_list(request):
    product_list = Product.objects.order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(product_list, 6)
    object_list = paginator.get_page(page)

    context = {
        'product_list': object_list,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all(),
        'no_category_product_count': Product.objects.filter(category=None).count(),
        'no_brand_product_count': Product.objects.filter(brand=None).count(),
        'current_page': 'shop',
    }

    return render(request, "shop/shop_list_jp.html", context)

# 商品詳細
def shop_detail(request, pk):
    product = Product.objects.get(id=pk)
    review_form = ReviewForm
    inquiry_form = InquiryForm
    like_count = Like.objects.filter(product=pk).count()
    like = Like.objects.filter(user=request.user.id, product=pk)
    review = Review.objects.filter(user=request.user.id, product=pk)

    return render(
        request,
        'shop/shop_detail_jp.html',
        {
            'product': product,
            'review_form': review_form,
            'inquiry_form': inquiry_form,
            'like_count': like_count,
            'like': like,
            'review': review,
            'current_page': 'shop',
        }
    )

# 商品検索
def search(request):
    q=request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 6)
    object_list = paginator.get_page(page)
    return render(request,
                  'shop/shop_search_list_jp.html',
                  {
                      'data': object_list,
                      'brands': Brand.objects.all(),
                      'categories': Category.objects.all(),
                      'no_category_product_count': Product.objects.filter(category=None).count(),
                      'no_brand_product_count': Product.objects.filter(brand=None).count(),
                      'current_page': 'shop',
                  }
            )

# レビュー登録
"""
def review_page(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        rating = request.POST['rating']
        content = request.POST['content']

        obj = Review.objects.create(
            content=content,
            rate=rating,
            user=request.user,
            product=product,
        )
        obj.save()
        return redirect('shop:shop_detail', pk)
"""


# レビューリスト
@csrf_protect
def review_list(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        review_list = Review.objects.filter(product_id=product_id)

        review_dict = []
        for review in review_list:
            user = User.objects.get(pk=review.user.id)

            review_arr = {
                'rate': review.rate,
                'content': review.content,
                'created_at': review.created_at,
                'profile_img': str(user.profile_img),
                'nickname': user.nickname,
                'user_id': user.id,
                'review_id': review.id,
            }
            review_dict.append(review_arr)

        return JsonResponse({'review_list': review_dict})


# レビュー情報
@csrf_protect
def review_read(request):
    if request.method == 'GET':
        review_id = request.GET.get('review_id')
        review = Review.objects.get(pk=review_id)

        review_arr = {
            'rate': review.rate,
            'content': review.content,
            'review_id': review.id,
        }
        return JsonResponse({'review': review_arr})


# レビュー登録
@csrf_protect
def review_create(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        rating = request.POST.get('rating')
        content = request.POST.get('content')
        product = Product.objects.get(id=product_id)

        obj = Review.objects.create(
            content=content,
            rate=rating,
            user=request.user,
            product=product,
        )
        obj.save()
        return JsonResponse({'result': 'ok'})


# レビュー修正
@csrf_protect
def review_update(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        rating = request.POST.get('rating')
        content = request.POST.get('content')
        review = Review.objects.get(pk=review_id)
        review.rate = rating
        review.content = content
        review.save()
        return JsonResponse({'result': 'ok'})


# レビュー削除
@csrf_protect
def review_delete(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = Review.objects.get(pk=review_id)
        review.delete()
        return JsonResponse({'result': 'ok'})


# お問い合わせリスト
@csrf_protect
def inquiry_list(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        inquiry_list = Inquiry.objects.filter(product_id=product_id)

        inquiry_dict = []
        for inquiry in inquiry_list:
            user = User.objects.get(pk=inquiry.user.id)

            inquiry_arr = {
                'content': inquiry.content,
                'created_at': inquiry.created_at,
                'profile_img': str(user.profile_img),
                'nickname': user.nickname,
                'user_id': user.id,
                'inquiry_id': inquiry.id,
                'admin_answer' : inquiry.answer,
                'admin_answered' : inquiry.answered,
            }
            inquiry_dict.append(inquiry_arr)

        return JsonResponse({'inquiry_list': inquiry_dict})


# お問い合わせ情報
@csrf_protect
def inquiry_read(request):
    if request.method == 'GET':
        inquiry_id = request.GET.get('inquiry_id')
        inquiry = Inquiry.objects.get(pk=inquiry_id)

        inquiry_arr = {
            'content': inquiry.content,
            'inquiry_id': inquiry.id,
        }
        return JsonResponse({'inquiry': inquiry_arr})


# お問い合わせ登録
@csrf_protect
def inquiry_create(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        content = request.POST.get('content')
        product = Product.objects.get(id=product_id)

        obj = Inquiry.objects.create(
            content=content,
            user=request.user,
            product=product,
        )
        obj.save()
        return JsonResponse({'result': 'ok'})


# お問い合わせ修正
@csrf_protect
def inquiry_update(request):
    if request.method == 'POST':
        inquiry_id = request.POST.get('inquiry_id')
        content = request.POST.get('content')
        inquiry = Inquiry.objects.get(pk=inquiry_id)
        inquiry.content = content
        inquiry.save()
        return JsonResponse({'result': 'ok'})


# お問い合わせ削除
@csrf_protect
def inquiry_delete(request):
    if request.method == 'POST':
        inquiry_id = request.POST.get('inquiry_id')
        inquiry = Inquiry.objects.get(pk=inquiry_id)
        inquiry.delete()
        return JsonResponse({'result': 'ok'})




"""
# お問い合わせ登録

def inquiry_page(request, pk):
    product = Product.objects.get(id=pk)
    category = Category.objects.all()
    no_category_product_count = Product.objects.filter(category=None).count()
    #    review_form = ReviewForm
    like_count = Like.objects.filter(product=pk).count()
    inquiry_form = InquiryForm
    if request.method == 'POST':
        inquiry_form = InquiryForm(request.POST)
        content = request.POST['content']

        obj = Inquiry.objects.create(
            content=content,
            user=request.user,
            product=product,
        )
        obj.save()
        return redirect('shop:shop_detail', pk)
"""

"""
@csrf_protect
def inquiry_list(request):
    if request.method == 'GET':
        pk = request.GET.get('pk')

        inquiry_list = Inquiry.objects.filter(product=pk)

        inquiry_dict = []
        for inquiry in inquiry_list:
            user = User.objects.get(pk=inquiry.user.id)

            inquiry_arr = {
                'content': inquiry.content,
                'created_at': inquiry.created_at,
                'profile_img': str(user.profile_img),
                'nickname': user.nickname,
                'answer': inquiry.answer,
                'answered': inquiry.answered,
            }
            inquiry_dict.append(inquiry_arr)

        return JsonResponse({'inquiry_list': inquiry_dict})


@csrf_protect
def inquiry_create(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        product = Product.objects.get(id=pk)
        content = request.POST['content']

        obj = Inquiry.objects.create(
            content=content,
            user=request.user,
            product=product,
        )
        obj.save()
        return JsonResponse({'result': 'ok'})


@csrf_protect
def inquiry_delete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        product = Product.objects.get(id=pk)
        content = request.POST['content']

        obj = Inquiry.objects.get_or_create(
            content=content,
            user=request.user,
            product=product,
        )
        obj.delete()
        return JsonResponse({'result': 'ok'})
"""

# いいね　登録
def like_page(request, pk):
    product = Product.objects.get(id=pk)
    review_form = ReviewForm
    inquiry_form = InquiryForm
    like = Like.objects.create(product=product, user=request.user)
    product.like_count += 1
    product.save()
    like_count = Like.objects.filter(product=pk).count()
    return redirect('shop:shop_detail', pk)


# いいね　キャンセル
def unlike_page(request, pk):
    product = Product.objects.get(id=pk)
    review_form = ReviewForm
    inquiry_form = InquiryForm
    Like.objects.filter(user=request.user.id, product=pk).delete()
    product.like_count -= 1
    product.save()
    like_count = Like.objects.filter(product=pk).count()
    return redirect('shop:shop_detail', pk)


#　カテゴリー
def category_page(request, slug):
    if slug == 'no_category':
        category = 'その他'
        shop_list = Product.objects.filter(category=None).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(shop_list, 6)
        object_list = paginator.get_page(page)
    else:
        category = Category.objects.get(slug=slug)
        shop_list = Product.objects.filter(category=category).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(shop_list, 6)
        object_list = paginator.get_page(page)

    return render(
        request,
        'shop/shop_list_jp.html',
        {
            'product_list': object_list,
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'no_category_product_count': Product.objects.filter(category=None).count(),
            'no_brand_product_count': Product.objects.filter(brand=None).count(),
            'category': category,
            'current_page': 'shop',
        }
    )


# ブランド
def brand_page(request, slug):
    if slug == 'no_brand':
        brand = '無印良品'
        shop_list = Product.objects.filter(brand=None).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(shop_list, 6)
        object_list = paginator.get_page(page)
    else:
        brand = Brand.objects.get(slug=slug)
        shop_list = Product.objects.filter(brand=brand).order_by('-created_at')
        page = request.GET.get('page', 1)
        paginator = Paginator(shop_list, 6)
        object_list = paginator.get_page(page)

    return render(
        request,
        'shop/shop_list_jp.html',
        {
            'product_list': object_list,
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'no_category_product_count': Product.objects.filter(category=None).count(),
            'no_brand_product_count': Product.objects.filter(brand=None).count(),
            'brand': brand,
            'current_page': 'shop',
        }

    )


# カート
def cart_list(request):
    cart_list = Cart.objects.filter(user=request.user).order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(cart_list, 4)
    object_list = paginator.get_page(page)

    cart_select = Cart.objects.filter(user=request.user).count()
    total_price = 0
    for each_total in cart_list:
        total_price += each_total.product.price * each_total.product_qty
    sale_price = int(total_price * 0.15)
    final_price = int(total_price * 0.85)
    
    return render(request,
                  'shop/cart_list_jp.html',
                  {
                      'cart_list': object_list,
                      'total_cart': total_price,
                      'sale_price': sale_price,
                      'cart_sum': final_price,
                      'cart_count': cart_select,
                      'current_page': 'my',
                  }
                  )


# カートに商品追加
def add_cart(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        product_qty_one = int(request.POST['quantity'])
        if Cart.objects.filter(product=product, user=request.user):
            messages.warning(request, 'すでにカートにある商品です。')
            return redirect('/shop/' + str(pk))
        else:
            Cart.objects.create(product=product, user=request.user, product_qty=product_qty_one)
            return redirect('/shop/cart_list/')
            
            
        
      

'''
# カートの商品削除
def remove_cart(request, pk):
    Cart.objects.filter(id=pk).delete()
    cart_list = Cart.objects.filter(user=request.user).order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(cart_list, 4)
    object_list = paginator.get_page(page)
    cart_select = Cart.objects.filter(user=request.user).count()
    total_price = 0
    for each_total in cart_list:
        total_price += each_total.product.price * each_total.product_qty
    sale = int(total_price * 0.15)
    final_price = int(total_price * 0.85)

    return render(
        request, 'shop/cart_list_jp.html',
        {
            'cart_list': object_list,
            'total_cart': total_price,
            'sale_price': sale,
            'cart_sum': final_price,
            'cart_count': cart_select,
            'current_page': 'my',
        }
    )
    
    
### Ajax 適用X
# カートプラスボタンクリック
def cart_plus_btn(request, pk):
    cart = Cart.objects.get(id=pk, user=request.user)
    cart.product_qty += 1
    cart.save()
    
    return JsonResponse({'result': 'ok',
                         'product_qty': cart.product_qty,
                         })

#  カートマイナスボタンクリック
def cart_minus_btn(request, pk):
    cart = Cart.objects.get(id=pk, user=request.user)
    if cart.product_qty > 1:
        cart.product_qty -= 1
    cart.save()
    return redirect('/shop/cart_list/')
'''

#Ajax カートプラスボタンクリック
def plus_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            if cart.product_qty < 10:
               cart.product_qty += 1
            cart.save()
            sub_total = int(cart.product_qty * cart.product.price)
            cart_list = Cart.objects.filter(user=request.user)
            total_price = 0
            for each_total in cart_list:
               total_price += each_total.product.price * each_total.product_qty
            sale = int(total_price * 0.15)
            final_price = int(total_price * 0.85)
            return JsonResponse({'result': 'success',
                                 'prod_price': sub_total,
                                 'total_price': total_price,
                                 'sale_price': sale,
                                 'calculate': final_price
                                 })
    return redirect('/')

#Ajax カートマイナスボタンクリック
def minus_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            if cart.product_qty > 1:
               cart.product_qty -= 1
            cart.save()
            sub_total = int(cart.product_qty * cart.product.price)
            cart_list = Cart.objects.filter(user=request.user)
            total_price = 0
            for each_total in cart_list:
               total_price += each_total.product.price * each_total.product_qty
            sale = int(total_price * 0.15)
            final_price = int(total_price * 0.85)
            return JsonResponse({'result': 'success',
                                 'prod_price': sub_total,
                                 'total_price': total_price,
                                 'sale_price': sale,
                                 'calculate': final_price
                                 })
    return redirect('/')

#Ajax 削除ボタン
def remove_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart_item = Cart.objects.get(product_id=prod_id, user=request.user)
            cart_item.delete()
            messages.info(request, 'カートリストから削除されました。')
            return JsonResponse({'result': 'success'})
    return redirect('/')
            

# お気に入りリスト
def wish_list(request):
    my_wish = Like.objects.filter(user=request.user).order_by('-pk')
    page = request.GET.get('page', 1)
    paginator = Paginator(my_wish, 6)
    object_list = paginator.get_page(page)
    return render(
        request,
        'shop/my_wish_list_jp.html',
        {
            'wish_list': object_list,
            'current_page': 'my',
        }
    )