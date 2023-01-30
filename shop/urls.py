from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
   
    path('search/', views.search, name='search'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),
    path('<int:pk>/like/', views.like_page, name='like_page'),
    path('<int:pk>/unlike/', views.unlike_page, name='unlike_page'),

    # 리뷰
    path('review_list/', views.review_list, name='review_list'),
    path('review_read/', views.review_read, name='review_read'),
    path('review_create/', views.review_create, name='review_create'),
    path('review_update/', views.review_update, name='review_update'),
    path('review_delete/', views.review_delete, name='review_delete'),
    
    # 문의
    path('inquiry_list/', views.inquiry_list, name='inquiry_list'),
    path('inquiry_read/', views.inquiry_read, name='inquiry_read'),
    path('inquiry_create/', views.inquiry_create, name='inquiry_create'),
    path('inquiry_update/', views.inquiry_update, name='inquiry_update'),
    path('inquiry_delete/', views.inquiry_delete, name='inquiry_delete'),

    path('category/<str:slug>/', views.category_page),
    path('brand/<str:slug>/', views.brand_page),
    path('cart_list/', views.cart_list, name='cart_list'),
    path('<int:pk>/add_cart/', views.add_cart, name='add_cart'),

    #path('<int:pk>/remove_cart/', views.remove_cart, name='remove_cart'),
    # 장바구니 플러스/마이너스 버튼 클릭시 Ajax 적용 X
    # path('plus_cart/<int:pk>/', views.cart_plus_btn, name='cart_plus_btn'),
    # path('minus_cart/<int:pk>/', views.cart_minus_btn, name='cart_minus_btn'),
    
    # 장바구니 Ajax 처리
    path('plus-cart/', views.plus_cart, name='plus_cart'),
    path('minus-cart/', views.minus_cart, name='minus_cart'),
    path('delete-cart/', views.remove_cart, name='delete_cart'),

    path('<int:pk>/remove_cart/', views.remove_cart, name='remove_cart'),

    # 좋아요 상품 리스트
    path('my_wish_list/', views.wish_list, name='wish_list'),

]