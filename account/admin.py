from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(User, UserAdmin) # 관리자 화면에서 CustomUser 모델 관리 가능
