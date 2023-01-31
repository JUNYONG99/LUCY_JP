from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


def signup(request):
    if request.method == 'POST':
        # 会員登録データ入力完了
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'account/signup_done_jp.html', {'new_user': new_user})

    else:
        form = UserCreationForm()
    return render(request, 'account/signup_jp.html', {'form': form})


# 会員ページ
def profile(request):
    return render(
        request,
        'account/profile_jp.html',
        {
          'current_page': 'my'
        }
    )


# プロフィール修正
def profile_update(request):
    if request.method == 'POST':
        profile = request.FILES.get('profile')
        if profile == None:
            messages.warning(request, '変更する写真を選択してください。')
            return redirect('/account/profile_jp/')

        img_update = User.objects.get(id=request.user.id)
        img_update.profile_img = profile
        img_update.save()
        messages.success(request, 'プロフィールが修正されました。')

    return redirect('/account/profile_jp/')


# プロフィール削除
def profile_delete(request):
    img_delete = User.objects.get(id=request.user.id)
    if not img_delete.profile_img:
        messages.warning(request, '登録するする写真がありません。')
        return redirect('/account/profile_jp/')

    img_delete.profile_img = None
    img_delete.save()
    messages.info(request, 'プロフィールをを削除しました。')

    return redirect('/account/profile_jp/')


# 名前・ニックネーム修正
def user_update(request):
    if request.method == 'POST':
        user_update = User.objects.get(id=request.user.id)
        user_name = request.POST['name']
        user_nickname = request.POST.get('nickname')
        try:
            if user_update.nickname == user_nickname:
                raise Exception
            if User.objects.get(nickname=user_nickname):
                messages.warning(request, 'すでに使用中のニックネームです。')
                return redirect('/account/profile_jp/')
        except:
            if user_name and user_nickname:
                user_update.name = user_name
                user_update.nickname = user_nickname
                user_update.save()
                messages.success(request, '会員情報が修正されました。')
                return redirect('/account/profile_jp/')


# 連絡先修正
def address_update(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']

        if not phone:
            messages.warning(request, '修正する連絡先を入力してください。')
            return redirect('/account/profile_jp/')

        user = User.objects.get(id=request.user.id)
        user.phone = phone
        user.address = address
        user.save()
        messages.success(request, '連絡先が修正されました。')
        return redirect('account:profile')

# パスワード変更
def password_update(request):
    if request.method == 'POST':
        
        current_password = request.POST['current_password']
        
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST['password']
            if not new_password:
                messages.error(request, '新しいパスワードを入力してください。')
                return redirect('account:profile') 
            password_confirm = request.POST["password2"]
            if not password_confirm:
                messages.error(request, 'パスワードを確認してください。')
                return redirect('account:profile') 
            
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'パスワードが変更されました。')
                return redirect('account:profile')   

    messages.warning(request, '既存のパスワードが一致しません。')
    return redirect('account:profile')
    
