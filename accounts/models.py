from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class Account(AbstractUser):
    phone_number_validator = RegexValidator(
        '^\d{2,3}-\d{3,4}-\d{4}$',
        _('-와 12자 이하의 숫자만 사용합니다'),
        _('invalid phone_number')
    )
    phone_number = models.CharField(
        _('휴대폰 번호'),
        validators=[phone_number_validator],
        max_length=15,
        unique=True,
        null=True
    )

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    name = models.CharField(_('이름'), max_length=10, validators=[UnicodeUsernameValidator], null=True)
    gender = models.IntegerField(_('성별'), choices=GENDER_CHOICES, null=True)
    birth_data = models.DateField(_('생년월일'), null=True)

    # 도로명 주소
    si_do = models.CharField(_('시도명'), max_length=30, null=True)
    si_gun_goo = models.CharField(_('시군구명'), max_length=30, null=True)
    eup_myun_dong = models.CharField(_('읍면동명'), max_length=30, null=True)
    lee = models.CharField(_('법정리명'), max_length=30, null=True)

    road_name = models.CharField(_('도로명'), max_length=100, null=True)
    building_id = models.CharField(_('건물번호'), max_length=30, null=True)

    detail_address = models.CharField(_('상세주소'), max_length=200, null=True)

    class Meta:
        verbose_name = _('사용자')
        verbose_name_plural = _('사용자')
