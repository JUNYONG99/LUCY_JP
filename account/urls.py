from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login_jp.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #마이 페이지 정보
    path('profile/', views.profile, name='profile'),
    #프로필 정보 
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
    #계정정보 수정
    path('profile/user_info/', views.user_update, name='user_info'),
    #연락처 정보 수정
    path('profile/address_update/', views.address_update, name='address_update'),
    #비밀번호 수정
    path('profile/password_update', views.password_update, name='password_update'),
    
    
]