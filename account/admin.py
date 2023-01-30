from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    #목록
    list_display = ('email', 'name', 'nickname', 'address', 'phone' ,'last_login')
    list_filter = ('is_superuser',)
    search_fields = ('email', 'name', 'nickname', 'address', 'phone')
    ordering = ('email',)
    filter_horizontal = ()
 
    #수정
    form = UserChangeForm
    fieldsets = (
        ('인증', {
            'fields': ('email', 'password')
        }),
        ('정보', {
            'fields': ('name', 'nickname', 'address', 'phone', 'profile_img')
        }),
        ('권한', {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
    )
    
    #등록
    add_form = UserCreationForm
    add_fieldsets = (
        ('인증', {
            'fields': ('email', 'password1', 'password2')
        }),
        ('정보', {
            'fields': ('name', 'nickname', 'address', 'phone', 'profile_img'),
        }),
        ('권한', {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
    )
    
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
