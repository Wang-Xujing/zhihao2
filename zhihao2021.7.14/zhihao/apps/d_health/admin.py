from django.contrib import admin
from apps import *
from .models import *
from apps.basic.models import BasicInfo

IS_POPUP_VAR = '_popup'


# Register your models here.
class IncorrectLookupParameters(Exception):
    pass


@admin.register(ImmunizationInfo)
class ImmunizationInfoAdmin(admin.ModelAdmin):
    # show_full_result_count = False
    field_name = ImmunizationInfo()._meta.fields
    list_display = ['ele_id', 'pre_num', 'maker', 'vaccine']
    change_view_list = [('basic_id', 'ele_num')]
    list_filter = []
    exclude_display = ['belong', 'vaccine_id', 'id']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)

    ordering = ('-id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(drugbathInfo)
class drugbathInfoAdmin(admin.ModelAdmin):
    field_name = drugbathInfo()._meta.fields
    list_display = ['id', 'ele_id', 'pre_num', 'drug_maker', 'drug']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            # params = drugbathInfo.objects.filter(belong=request.user.belong).values('basic_id')
            # look_choice = []
            #
            # for i in list(params):
            #     basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("ele_num").first()
            #     temp = ('{}'.format(basic_ele['ele_num']), ('{}'.format(basic_ele['ele_num'])))
            #     if temp not in look_choice:
            #         look_choice.append(temp)
            look_choice = [('', '')]

            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(ele_num=value).values("id").first()
            return drugbathInfo.objects.filter(basic_id=basic['id']).all()

    class preFilter(admin.SimpleListFilter):
        title = "防疫耳号"
        parameter_name = 'pre_num'

        def lookups(self, request, model_admin):
            params = drugbathInfo.objects.filter(belong=request.user.belong).values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("pre_num").first()
                temp = ('{}'.format(basic_ele['pre_num']), ('{}'.format(basic_ele['pre_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(pre_num=value).values("id").first()
            return drugbathInfo.objects.filter(basic_id=basic['id']).all()

    list_filter =[]
    exclude_display = ['belong', 'vac_maker', 'drug_id']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_zhu.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(quarantineInfo)
class quarantineInfoAdmin(admin.ModelAdmin):
    field_name = quarantineInfo()._meta.fields
    list_display = ['id', 'ele_id', 'pre_num']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = quarantineInfo.objects.filter(belong=request.user.belong).values('basic_id')
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
            return quarantineInfo.objects.filter(basic_id=basic['id']).all()

    class preFilter(admin.SimpleListFilter):
        title = "防疫耳号"
        parameter_name = 'pre_num'

        def lookups(self, request, model_admin):
            params = quarantineInfo.objects.filter(belong=request.user.belong).values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("pre_num").first()
                temp = ('{}'.format(basic_ele['pre_num']), ('{}'.format(basic_ele['pre_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(pre_num=value).values("id").first()
            return quarantineInfo.objects.filter(basic_id=basic['id']).all()

    list_filter =[]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)


@admin.register(nursingInfo)
class nursingInfoAdmin(admin.ModelAdmin):
    field_name = nursingInfo()._meta.fields
    list_display = ['id', 'ele_id', 'pre_num']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = nursingInfo.objects.filter(belong=request.user.belong).values('basic_id')
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
            return nursingInfo.objects.filter(basic_id=basic['id']).all()

    class preFilter(admin.SimpleListFilter):
        title = "防疫耳号"
        parameter_name = 'pre_num'

        def lookups(self, request, model_admin):
            params = nursingInfo.objects.filter(belong=request.user.belong).values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("pre_num").first()
                temp = ('{}'.format(basic_ele['pre_num']), ('{}'.format(basic_ele['pre_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(pre_num=value).values("id").first()
            return nursingInfo.objects.filter(basic_id=basic['id']).all()

    list_filter =[]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_zhu.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(diseaseInfo)
class diseaseInfoAdmin(admin.ModelAdmin):
    field_name = diseaseInfo()._meta.fields
    list_display = ['id', 'ele_id', 'pre_num', 'drug']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = diseaseInfo.objects.filter(belong=request.user.belong).values('basic_id')
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
            return diseaseInfo.objects.filter(basic_id=basic['id']).all()

    class preFilter(admin.SimpleListFilter):
        title = "防疫耳号"
        parameter_name = 'pre_num'

        def lookups(self, request, model_admin):
            params = diseaseInfo.objects.filter(belong=request.user.belong).values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("pre_num").first()
                temp = ('{}'.format(basic_ele['pre_num']), ('{}'.format(basic_ele['pre_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(pre_num=value).values("id").first()
            return diseaseInfo.objects.filter(basic_id=basic['id']).all()

    list_filter =[]
    exclude_display = ['belong', 'drug_id']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_zhu.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('-id',)
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(deathInfo)
class deathInfoAdmin(admin.ModelAdmin):
    field_name = deathInfo()._meta.fields
    list_display = ['id', 'ele_id', 'pre_num']
    actions = None

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = deathInfo.objects.filter(belong=request.user.belong).values('basic_id')
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
            return deathInfo.objects.filter(basic_id=basic['id']).all()

    class preFilter(admin.SimpleListFilter):
        title = "防疫耳号"
        parameter_name = 'pre_num'

        def lookups(self, request, model_admin):
            params = deathInfo.objects.filter(belong=request.user.belong).values('basic_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['basic_id']).values("pre_num").first()
                temp = ('{}'.format(basic_ele['pre_num']), ('{}'.format(basic_ele['pre_num'])))
                if temp not in look_choice:
                    look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            basic = BasicInfo.objects.filter(pre_num=value).values("id").first()
            return deathInfo.objects.filter(basic_id=basic['id']).all()

    list_filter =[]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_no_actions.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    del list_display[0]
    ordering = ('-id',)
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
