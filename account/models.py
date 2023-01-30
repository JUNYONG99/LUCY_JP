from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, name, nickname, address=None, phone=None, profile_img=None, password=None):
        if not email:
            raise ValueError('사용자 이메일은 필수입니다.')
        if not name:
            raise ValueError('사용자 이름은 필수입니다.')
        if not nickname:
            raise ValueError('사용자 닉네임은 필수입니다.')
        """
        if not address:
            raise ValueError('사용자 주소는 필수입니다.')
        if not phone:
            raise ValueError('사용자 연락처는 필수입니다.')
        """

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            address=address,
            phone=phone,
            profile_img=profile_img,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, nickname, address=None, phone=None, profile_img=None, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            nickname=nickname,
            address=address,
            phone=phone,
            profile_img=profile_img,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    name = models.CharField(verbose_name="이름", max_length=24)
    nickname = models.CharField(verbose_name="닉네임", max_length=24, unique=True)
    address = models.CharField(verbose_name="주소", max_length=255, null=True)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(verbose_name="연락처", validators=[phoneNumberRegex], max_length=16, null=True)
    profile_img = models.ImageField(verbose_name="프로필 사진", upload_to='account/images/%Y/%m/%d/', null=True)
    last_login = models.DateTimeField(verbose_name="마지막 로그인 날짜", auto_now=True)
    is_active = models.BooleanField(verbose_name="로그인 가능 유무", default=True)
    is_superuser = models.BooleanField(verbose_name="최고관리자", default=False)
    is_staff = models.BooleanField(verbose_name="관리자페이지 접근", default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name', 'nickname', 'address', 'phone']
    REQUIRED_FIELDS = ['name', 'nickname']

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
