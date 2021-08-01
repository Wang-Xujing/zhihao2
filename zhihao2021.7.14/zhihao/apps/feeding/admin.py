from django.contrib import admin
from apps.feeding.models import feedHouseInfo
from apps.colony.models import HouseInfo
from apps import *
# Register your models here.

@admin.register(feedHouseInfo)
class disinfectionInfoAdmin(admin.ModelAdmin):
    field_name = feedHouseInfo()._meta.fields
    list_display = ['id','house']
    class pidFilter(admin.SimpleListFilter):
        title = "棚"
        parameter_name = 'pid_name'

        def lookups(self, request, model_admin):

            params = HouseInfo.objects.filter(pid=0).all().values('name')
            look_choice = []
            for i in list(params):
                temp = ('{}'.format(i['name']), ('{}'.format(i['name'])))
                look_choice.append(temp)
            return look_choice

        def queryset(self, request, queryset):
            # basic_ele = BasicInfo.objects.filter(id=i.basic_id).values("ele_num")
            value = self.value()
            if not value:
                return queryset
            peng = HouseInfo.objects.filter(name=value).values("id").first()
            house=HouseInfo.objects.filter(pid=peng['id']).all().values("id")
            cut=[]
            for i in list(house):
                cut.append(HouseInfo.objects.filter(id=i['id']))
            return cut
    list_filter = []
    exclude_display = ['belong','house_id','id']
    exclude_filter = []
    search_fields = []
    change_list_template = 'change_list_zhu.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    # del list_display[0]
    ordering = ('id',)
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
