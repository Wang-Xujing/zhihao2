from django.contrib import admin
from . models import *
from apps import *
from .models import *
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    field_name = Inventory()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    #readonly_fields = ('total',)

class Vaccine_inAdmin(admin.ModelAdmin):
    field_name = Vaccine_in()._meta.fields
    list_display = ['maker']
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


class Vaccine_outAdmin(admin.ModelAdmin):
    field_name = Vaccine_out()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)

class Feedingin_Admin(admin.ModelAdmin):
    field_name = Feedingin()._meta.fields
    list_display = ['maker']
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

class Feeding_outAdmin(admin.ModelAdmin):
    field_name = Feeding_out()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)



admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Vaccine_in, Vaccine_inAdmin)
admin.site.register(Vaccine_out, Vaccine_outAdmin)
admin.site.register(Feedingin,  Feedingin_Admin)
admin.site.register(Feeding_out, Feeding_outAdmin)


