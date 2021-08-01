from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'realname','jobrole', 'mobile','id_card', 'qq', 'weChat', 'addr','staff_num','belong']
    # �޸��û�ʱ�����real_name,mobile��qq��weChat,addr��¼��
    # ��Դ���UserAdmin.fieldsetsת�����б��ʽ
    fieldsets = list(UserAdmin.fieldsets)
    # ��дUserAdmin��fieldsets�����mobile��qq��weChat��¼��
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('realname','jobrole', 'mobile','id_card', 'addr','staff_num','belong')})
    add_fieldsets=(
        (None, {'fields': ('username', 'password1','password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','realname', 'staff_num','email','jobrole', 'mobile','id_card','qq','weChat', 'addr','belong')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
