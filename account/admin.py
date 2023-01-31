from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    #リスト
    list_display = ('email', 'name', 'nickname', 'address', 'phone' ,'last_login')
    list_filter = ('is_superuser',)
    search_fields = ('email', 'name', 'nickname', 'address', 'phone')
    ordering = ('email',)
    filter_horizontal = ()
 
    #修正
    form = UserChangeForm
    fieldsets = (
        ('認証', {
            'fields': ('email', 'password')
        }),
        ('情報', {
            'fields': ('name', 'nickname', 'address', 'phone', 'profile_img')
        }),
        ('権限.', {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
    )
    
    #登録
    add_form = UserCreationForm
    add_fieldsets = (
        ('認証', {
            'fields': ('email', 'password1', 'password2')
        }),
        ('情報', {
            'fields': ('name', 'nickname', 'address', 'phone', 'profile_img'),
        }),
        ('権限', {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
    )
    
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
