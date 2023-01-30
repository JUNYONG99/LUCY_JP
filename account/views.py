from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


def signup(request):
    if request.method == 'POST':
        # 회원 가입 데이터 입력 완료
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'account/signup_done_jp.html', {'new_user': new_user})

    else:
        form = UserCreationForm()
    return render(request, 'account/signup_jp.html', {'form': form})


# 마이 페이지
def profile(request):
    return render(
        request,
        'account/profile_jp.html',
        {
          'current_page': 'my'
        }
    )


# 프로필 수정
def profile_update(request):
    if request.method == 'POST':
        profile = request.FILES.get('profile')
        if profile == None:
            messages.warning(request, '변경 하실 사진을 선택해주세요.')
            return redirect('/account/profile_jp/')

        img_update = User.objects.get(id=request.user.id)
        img_update.profile_img = profile
        img_update.save()
        messages.success(request, '프로필 이미지가 수정되었습니다.')

    return redirect('/account/profile_jp/')


# 프로필 삭제
def profile_delete(request):
    img_delete = User.objects.get(id=request.user.id)
    if not img_delete.profile_img:
        messages.warning(request, '프로필 사진이 없습니다.')
        return redirect('/account/profile_jp/')

    img_delete.profile_img = None
    img_delete.save()
    messages.info(request, '프로필 이미지를 삭제하였습니다.')

    return redirect('/account/profile_jp/')


# 계정 이름 / 닉네임 변경
def user_update(request):
    if request.method == 'POST':
        user_update = User.objects.get(id=request.user.id)
        user_name = request.POST['name']
        user_nickname = request.POST.get('nickname')
        try:
            if user_update.nickname == user_nickname:
                raise Exception
            if User.objects.get(nickname=user_nickname):
                messages.warning(request, '이미 사용중인 닉네임입니다.')
                return redirect('/account/profile_jp/')
        except:
            if user_name and user_nickname:
                user_update.name = user_name
                user_update.nickname = user_nickname
                user_update.save()
                messages.success(request, '계정정보가 수정되었습니다.')
                return redirect('/account/profile_jp/')


# 연락처 업데이트
def address_update(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']

        if not phone:
            messages.warning(request, '수정하실 연락처를 입력해주세요.')
            return redirect('/account/profile_jp/')

        user = User.objects.get(id=request.user.id)
        user.phone = phone
        user.address = address
        user.save()
        messages.success(request, '연락처가 수정되었습니다.')
        return redirect('account:profile')

# 비밀번호 변경
def password_update(request):
    if request.method == 'POST':
        
        current_password = request.POST['current_password']
        
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST['password']
            if not new_password:
                messages.error(request, '새 비밀번호를 입력해주세요.')
                return redirect('account:profile') 
            password_confirm = request.POST["password2"]
            if not password_confirm:
                messages.error(request, '비밀번호를 확인해주세요.')
                return redirect('account:profile') 
            
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, '비밀번호가 변경되었습니다.')
                return redirect('account:profile')   

    messages.warning(request, '현재 비밀번호가 일치하지 않습니다.')
    return redirect('account:profile')
    
