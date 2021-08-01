from django.contrib import admin
from .models import *
from apps import *
from apps.basic.models import BasicInfo
# Register your models here.

@admin.register(economicInfo)
class economicInfoAdmin(admin.ModelAdmin):
    field_name = economicInfo()._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = economicInfo.objects.all().values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("ele_num").first()
                temp = ('{}'.format(basic_ele['ele_num']), ('{}'.format(basic_ele['ele_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(ele_num=value).values("id").first()
            return economicInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(S_salesInfo)
class S_salesInfoAdmin(admin.ModelAdmin):
    field_name = S_salesInfo()._meta.fields
    list_display = ['id']
    actions = None
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_no_actions.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(G_salesInfo)
class G_salesInfoAdmin(admin.ModelAdmin):
    field_name = G_salesInfo._meta.fields
    list_display = ['id']


    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(SlaughterSegmentInfo)
class SlaughterSegmentInfoAdmin(admin.ModelAdmin):
    field_name = SlaughterSegmentInfo._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = SlaughterSegmentInfo.objects.all().values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("ele_num").first()
                temp = ('{}'.format(basic_ele['ele_num']), ('{}'.format(basic_ele['ele_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(ele_num=value).values("id").first()
            return SlaughterSegmentInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'g_slaughter/test_SlaughterSegmentInfo.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(BinformationInfo)
class BinformationInfoAdmin(admin.ModelAdmin):
    field_name = BinformationInfo._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = BinformationInfo.objects.all().values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("ele_num").first()
                temp = ('{}'.format(basic_ele['ele_num']), ('{}'.format(basic_ele['ele_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(ele_num=value).values("id").first()
            return BinformationInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

