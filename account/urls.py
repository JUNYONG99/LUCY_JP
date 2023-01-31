from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login_jp.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #会員ページ
    path('profile_jp/', views.profile, name='profile'),
    #プロフィール
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    #会員情報修正
    path('profile/user_info/', views.user_update, name='user_info'),
    #連絡先修正
    path('profile/address_update/', views.address_update, name='address_update'),
    #パスワード変更
    path('profile/password_update', views.password_update, name='password_update'),
    
    
]