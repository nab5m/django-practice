# Generated by Django 3.0.4 on 2020-03-18 15:09

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator('^\\d{2,3}-\\d{3,4}-\\d{4}$', '-와 12자 이하의 숫자만 사용합니다', 'invalid phone_number')], verbose_name='휴대폰 번호')),
                ('name', models.CharField(max_length=10, validators=[django.contrib.auth.validators.UnicodeUsernameValidator], verbose_name='이름')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], verbose_name='성별')),
                ('birth_data', models.DateField(verbose_name='생년월일')),
                ('si_do', models.CharField(blank=True, max_length=30, verbose_name='시도명')),
                ('si_gun_goo', models.CharField(blank=True, max_length=30, verbose_name='시군구명')),
                ('eup_myun_dong', models.CharField(blank=True, max_length=30, verbose_name='읍면동명')),
                ('lee', models.CharField(blank=True, max_length=30, verbose_name='법정리명')),
                ('road_name', models.CharField(blank=True, max_length=100, verbose_name='도로명')),
                ('building_id', models.CharField(blank=True, max_length=30, verbose_name='건물번호')),
                ('detail_address', models.CharField(blank=True, max_length=200, verbose_name='상세주소')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
