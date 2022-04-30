from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser): # User 모델 확장을 위한 AbstractUser 상속

    GENDER_CHOICES=(
        ('남','남'),
        ('여','여'),
    )# 성별을 선택하게 하기 위함

    nickname = models.CharField(max_length=20,unique=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    #phone = PhoneNumberField(null=False, blank=False)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex],max_length=11,unique=True)
    def __str__(self):
        return self.nickname