from django.contrib import admin
# Register your models here.
from . models import *
from apps import *

#    fields = []  修改添加字段的顺序

class v_suppliersInfoAdmin(admin.ModelAdmin):
    field_name = v_suppliersInfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

class f_suppliersInfoAdmin(admin.ModelAdmin):
    field_name = f_suppliersInfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
class insuranceinfoAdmin(admin.ModelAdmin):
    field_name = insuranceinfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
class commodityInfoAdmin(admin.ModelAdmin):
    field_name = commodityInfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
admin.site.register(v_suppliersInfo, v_suppliersInfoAdmin)
admin.site.register(f_suppliersInfo, f_suppliersInfoAdmin)
admin.site.register(insuranceinfo, insuranceinfoAdmin)
admin.site.register(commodityInfo, commodityInfoAdmin)
