from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'nickname', 'address', 'phone')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="비밀번호",
        help_text = ("<a href='../password/'>[비밀번호 변경]</a>")
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'nickname', 'address', 'phone', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]
    


        
    