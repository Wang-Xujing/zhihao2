from django.contrib import admin
from .models import *
from apps import *
from django.http import HttpResponse
from apps.basic.models import BasicInfo
# Register your models here.
##options
from django.utils.datastructures import MultiValueDictKeyError
import copy
import json
import operator
import re
from functools import partial, reduce, update_wrapper
from urllib.parse import quote as urlquote
from django.contrib.admin import actions as ac
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.admin import helpers, widgets
from django.contrib.admin.checks import (
    BaseModelAdminChecks, InlineModelAdminChecks, ModelAdminChecks,
)
from django.contrib.admin.exceptions import DisallowedModelAdminToField
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.admin.utils import (
    NestedObjects, construct_change_message, flatten_fieldsets,
    get_deleted_objects, lookup_needs_distinct, model_format_dict,
    model_ngettext, quote, unquote,
)
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from django.contrib.admin.widgets import (
    AutocompleteSelect, AutocompleteSelectMultiple,
)
from django.contrib.auth import get_permission_codename
from django.core.exceptions import (
    FieldDoesNotExist, FieldError, PermissionDenied, ValidationError,
)
from django.core.paginator import Paginator
from django.db import models, router, transaction
from django.db.models.constants import LOOKUP_SEP
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.formsets import DELETION_FIELD_NAME, all_valid
from django.forms.models import (
    BaseInlineFormSet, inlineformset_factory, modelform_defines_fields,
    modelform_factory, modelformset_factory,
)
from django.forms.widgets import CheckboxSelectMultiple, SelectMultiple
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseBase
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst, format_lazy, get_text_list
from django.utils.translation import gettext as _, ngettext
from django.views.decorators.csrf import csrf_protect
from django.views.generic import RedirectView
from apps.e_breed.models import *

IS_POPUP_VAR = '_popup'


@admin.register(rutInfo)
class rutInfoAdmin(admin.ModelAdmin):
    field_name = rutInfo()._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = rutInfo.objects.all().values('basic_id')
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
            return rutInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test-rutinfo.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(SemencollectInfo)
class SemencollectInfoAdmin(admin.ModelAdmin):
    field_name = SemencollectInfo()._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = SemencollectInfo.objects.all().values('basic_id')
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
            return SemencollectInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test-semencollectinfo.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(breedingInfo)
class breedingInfoAdmin(admin.ModelAdmin):
    field_name = breedingInfo()._meta.fields
    list_display = ['ele_id_ewe', 'ele_id_ram']

    class eweFilter(admin.SimpleListFilter):

        title = "母羊耳号"
        parameter_name = 'ewe_id'

        def lookups(self, request, model_admin):
            params = breedingInfo.objects.all().values('ewe_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['ewe_id']).values("ele_num").first()
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
            return breedingInfo.objects.filter(ewe_id=basic['id']).all()

    class ramFilter(admin.SimpleListFilter):

        title = "公羊耳号"
        parameter_name = 'ram_id'

        def lookups(self, request, model_admin):
            params = breedingInfo.objects.all().values('ram_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['ram_id']).values("ele_num").first()
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
            return breedingInfo.objects.filter(ram_id=basic['id']).all()

    list_filter = [eweFilter, ramFilter]

    exclude_display = ['belong', 'ewe_id', 'ram_id']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'e_breed/test_breedinginfo.html'
    change_list_template_page = 'test_change_list.html'

    def _changeform_view(self, request, object_id, form_url, extra_context):
        ##########
        from apps.basic.models import BasicInfo
        import datetime
        request_copy = request.POST.copy()
        basic_ids = []
        many_add = False
        if request.method == "POST":

            try:
                if len(request_copy['many-basic_basicinfo_ewe']) > 0:
                    request_copy['ewe_id'] = request_copy['many-basic_basicinfo_ewe'][:-1]

                elif len(request_copy['basic_basicinfo_ewe']) > 0:
                    request_copy['ewe_id'] = \
                    BasicInfo.objects.filter(name=request_copy['basic_basicinfo_ewe']).values('id').first()['id']
                else:
                    pass
            except MultiValueDictKeyError:
                pass
            try:
                if len(request_copy['many-basic_basicinfo_ram']) > 0:
                    request_copy['ram_id'] = request_copy['many-basic_basicinfo_ram'][:-1]
                elif len(request_copy['basic_basicinfo_ram']) > 0:
                    request_copy['ram_id'] = \
                    BasicInfo.objects.filter(name=request_copy['basic_basicinfo_ram']).values('id').first()['id']
                else:
                    pass
            except MultiValueDictKeyError:
                pass
            print(BasicInfo.objects.filter(id=int(request_copy['ewe_id'])).first())
            request_copy['ewe_variety'] = \
            BasicInfo.objects.filter(id=int(request_copy['ewe_id'])).values('variety').first()['variety']
            request_copy['ram_variety'] = \
            BasicInfo.objects.filter(id=int(request_copy['ram_id'])).values('variety').first()['variety']
        request.POST = request_copy
        ###########
        to_field = request.POST.get('_to_field', request.GET.get('_to_field'))
        if to_field and not self.to_field_allowed(request, to_field):
            raise DisallowedModelAdminToField("The field %s cannot be referenced." % to_field)

        model = self.model
        opts = model._meta

        if request.method == 'POST' and '_saveasnew' in request.POST:
            object_id = None

        add = object_id is None

        if add:
            if not self.has_add_permission(request):
                raise PermissionDenied
            obj = None

        else:
            obj = self.get_object(request, unquote(object_id), to_field)

            if request.method == 'POST':
                if not self.has_change_permission(request, obj):
                    raise PermissionDenied
            else:
                if not self.has_view_or_change_permission(request, obj):
                    raise PermissionDenied

            if obj is None:
                return self._get_obj_does_not_exist_redirect(request, opts, object_id)

        ModelForm = self.get_form(request, obj, change=not add)
        #####
        if request.method == 'POST' and many_add:
            for i in basic_ids:
                request_copy = request.POST.copy()
                request_copy['basic_id'] = i
                ##月龄，药龄，年龄计算
                if 'imm_date' in request.POST:
                    birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                    imm_date = datetime.date(*map(int, request_copy['imm_date'].split('/')))
                    imm_age = imm_date - birth

                    request_copy['imm_age'] = round((imm_age.days) / 30, 1)
                elif 'drug_age' in request.POST:
                    birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                    drug_date = datetime.date(*map(int, request_copy['take_time'].split('/')))
                    drug_age = drug_date - birth
                    request_copy['drug_age'] = round((drug_age.days) / 30, 1)
                elif 'age' in request.POST:
                    birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                    birth = datetime.datetime.combine(birth, datetime.time())
                    now = datetime.datetime.now()
                    age = now - birth
                    request_copy['age'] = int(age.days / 365)
                else:
                    pass
                request.POST = request_copy
                print(request.POST)
                form = ModelForm(request.POST, request.FILES, instance=obj)
                form_validated = form.is_valid()
                if form_validated:
                    new_object = self.save_form(request, form, change=not add)
                else:
                    new_object = form.instance
                formsets, inline_instances = self._create_formsets(request, new_object, change=not add)
                if all_valid(formsets) and form_validated:
                    self.save_model(request, new_object, form, not add)
                    self.save_related(request, form, formsets, not add)
                    change_message = self.construct_change_message(request, form, formsets, add)
                    if add:
                        self.log_addition(request, new_object, change_message)
                    else:
                        self.log_change(request, new_object, change_message)
            return self.response_add(request, new_object)
        ####

        elif request.method == 'POST':
            ##月龄，药龄，年龄计算
            if 'imm_date' in request.POST:
                birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                imm_date = datetime.date(*map(int, request_copy['imm_date'].split('/')))
                imm_age = imm_date - birth
                request_copy['imm_age'] = round((imm_age.days) / 30, 2)
            elif 'drug_age' in request.POST:
                birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                drug_date = datetime.date(*map(int, request_copy['take_time'].split('/')))
                drug_age = drug_date - birth
                request_copy['drug_age'] = round((drug_age.days) / 30, 2)
            elif 'age' in request.POST:
                birth = BasicInfo.objects.filter(id=int(request_copy['basic_id'])).values('birth').first()['birth']
                birth = datetime.datetime.combine(birth, datetime.time())
                now = datetime.datetime.now()
                age = now - birth
                request_copy['age'] = int(age.days / 365)
            else:
                pass
            form = ModelForm(request.POST, request.FILES, instance=obj)
            form_validated = form.is_valid()
            if form_validated:
                new_object = self.save_form(request, form, change=not add)
            else:
                new_object = form.instance
            formsets, inline_instances = self._create_formsets(request, new_object, change=not add)
            if all_valid(formsets) and form_validated:
                self.save_model(request, new_object, form, not add)
                self.save_related(request, form, formsets, not add)
                change_message = self.construct_change_message(request, form, formsets, add)
                if add:
                    self.log_addition(request, new_object, change_message)
                    return self.response_add(request, new_object)
                else:
                    self.log_change(request, new_object, change_message)
                    return self.response_change(request, new_object)
            else:
                form_validated = False
        else:
            if add:
                initial = self.get_changeform_initial_data(request)
                form = ModelForm(initial=initial)
                formsets, inline_instances = self._create_formsets(request, form.instance, change=False)
            else:
                form = ModelForm(instance=obj)

                formsets, inline_instances = self._create_formsets(request, obj, change=True)

        if not add and not self.has_change_permission(request, obj):
            readonly_fields = flatten_fieldsets(self.get_fieldsets(request, obj))
        else:
            readonly_fields = self.get_readonly_fields(request, obj)
        adminForm = helpers.AdminForm(
            form,
            list(self.get_fieldsets(request, obj)),
            # Clear prepopulated fields on a view-only form to avoid a crash.
            self.get_prepopulated_fields(request, obj) if add or self.has_change_permission(request, obj) else {},
            readonly_fields,
            model_admin=self)

        media = self.media + adminForm.media

        inline_formsets = self.get_inline_formsets(request, formsets, inline_instances, obj)
        for inline_formset in inline_formsets:
            media = media + inline_formset.media

        if add:
            title = _('Add %s')
        elif self.has_change_permission(request, obj):
            title = _('Change %s')
        else:
            title = _('View %s')
        IS_POPUP_VAR = '_popup'
        context = {
            **self.admin_site.each_context(request),
            'title': title % opts.verbose_name,
            'adminform': adminForm,
            # 'open_addPage':[i[0] for i in self.open_addPage],
            # 'open_dict':open_dict,
            'object_id': object_id,
            'original': obj,
            'is_popup': IS_POPUP_VAR in request.POST or IS_POPUP_VAR in request.GET,
            'to_field': to_field,
            'media': media,
            'inline_admin_formsets': inline_formsets,
            'errors': helpers.AdminErrorList(form, formsets),
            'preserved_filters': self.get_preserved_filters(request),
        }

        # Hide the "Save" and "Save and continue" buttons if "Save as New" was
        # previously chosen to prevent the interface from getting confusing.
        if request.method == 'POST' and not form_validated and "_saveasnew" in request.POST:
            context['show_save'] = False
            context['show_save_and_continue'] = False
            # Use the change template instead of the add template.
            add = False

        context.update(extra_context or {})

        return self.render_change_form(request, context, add=add, change=not add, obj=obj, form_url=form_url)


@admin.register(pregnantInfo)
class pregnantInfoAdmin(admin.ModelAdmin):
    field_name = pregnantInfo()._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = pregnantInfo.objects.all().values('basic_id')
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
            return pregnantInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(postnatalInfo)
class postnatalInfoAdmin(admin.ModelAdmin):
    field_name = postnatalInfo()._meta.fields
    list_display = ['id', 'ele_id_ewe', 'ele_id_ram']

    class eweFilter(admin.SimpleListFilter):

        title = "母羊耳号"
        parameter_name = 'ewe_id'

        def lookups(self, request, model_admin):
            params = postnatalInfo.objects.all().values('ewe_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['ewe_id']).values("ele_num").first()
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
            return postnatalInfo.objects.filter(ewe_id=basic['id']).all()

    class ramFilter(admin.SimpleListFilter):

        title = "公羊耳号"
        parameter_name = 'ram_id'

        def lookups(self, request, model_admin):
            params = postnatalInfo.objects.all().values('ram_id')
            look_choice = []
            for i in list(params):
                basic_ele = BasicInfo.objects.filter(id=i['ram_id']).values("ele_num").first()
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
            return postnatalInfo.objects.filter(ram_id=basic['id']).all()

    list_filter = [eweFilter, ramFilter]
    exclude_display = ['belong', 'ewe_id', 'ram_id']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

    def _changeform_view(self, request, object_id, form_url, extra_context):
        ##########

        from apps.h_store.models import Vaccine_in
        from apps.supply.models import v_suppliersInfo
        from apps.basic.models import BasicInfo
        import datetime
        request_copy = request.POST.copy()
        basic_ids = []
        many_add = False
        if request.method == "POST":
            ###产后信息添加配种信息自动生成公羊母羊电子耳号
            try:
                from apps.e_breed.models import breedingInfo
                if len(request_copy['many-e_breed_breedinginfo']) > 0:
                    request_copy['breeding_id'] = request_copy['many-e_breed_breedinginfo'][:-1]
                    breed = breedingInfo.objects.filter(id=request_copy['breeding_id']).values().first()
                    request_copy['ewe_id'] = breed['ewe_id']
                    request_copy['ram_id'] = breed['ram_id']
                    request_copy['breeding_date'] = breed['breeding_date']
                else:
                    pass
            except MultiValueDictKeyError:
                pass
        request.POST = request_copy
        print(request.POST)
        ###########
        to_field = request.POST.get('_to_field', request.GET.get('_to_field'))
        if to_field and not self.to_field_allowed(request, to_field):
            raise DisallowedModelAdminToField("The field %s cannot be referenced." % to_field)

        model = self.model
        opts = model._meta

        if request.method == 'POST' and '_saveasnew' in request.POST:
            object_id = None

        add = object_id is None

        if add:
            if not self.has_add_permission(request):
                raise PermissionDenied
            obj = None

        else:
            obj = self.get_object(request, unquote(object_id), to_field)

            if request.method == 'POST':
                if not self.has_change_permission(request, obj):
                    raise PermissionDenied
            else:
                if not self.has_view_or_change_permission(request, obj):
                    raise PermissionDenied

            if obj is None:
                return self._get_obj_does_not_exist_redirect(request, opts, object_id)

        ModelForm = self.get_form(request, obj, change=not add)
        #####

        ####

        if request.method == 'POST':
            ##添加羔羊信息
            from apps.e_breed.models import LambInfo
            n = int(request.POST['live_num'])
            for i in range(1, n + 1):
                from apps.basic.models import BasicInfo
                basic_m = BasicInfo.objects.filter(id=request.POST['ewe_id']).values().first()
                basic_f = BasicInfo.objects.filter(id=request.POST['ram_id']).values().first()
                logo = basic_m['ele_num'] + '_' + request.POST['delivery_date'] + '_' + str(i)
                dict = {
                    'm_ele_num': basic_m['ele_num'],
                    'm_pre_num': basic_m['pre_num'],
                    'f_ele_num': basic_f['ele_num'],
                    'f_pre_num': basic_f['pre_num'],
                    'belong':request.POST['belong'],
                    'logo':logo
                }

                LambInfo.objects.create(**dict)
            form = ModelForm(request.POST, request.FILES, instance=obj)
            form_validated = form.is_valid()
            if form_validated:
                new_object = self.save_form(request, form, change=not add)
            else:
                new_object = form.instance
            formsets, inline_instances = self._create_formsets(request, new_object, change=not add)
            if all_valid(formsets) and form_validated:
                self.save_model(request, new_object, form, not add)
                self.save_related(request, form, formsets, not add)
                change_message = self.construct_change_message(request, form, formsets, add)
                if add:
                    self.log_addition(request, new_object, change_message)
                    return self.response_add(request, new_object)
                else:
                    self.log_change(request, new_object, change_message)
                    return self.response_change(request, new_object)
            else:
                form_validated = False
        else:
            if add:
                initial = self.get_changeform_initial_data(request)
                form = ModelForm(initial=initial)
                formsets, inline_instances = self._create_formsets(request, form.instance, change=False)
            else:
                form = ModelForm(instance=obj)

                formsets, inline_instances = self._create_formsets(request, obj, change=True)

        if not add and not self.has_change_permission(request, obj):
            readonly_fields = flatten_fieldsets(self.get_fieldsets(request, obj))
        else:
            readonly_fields = self.get_readonly_fields(request, obj)
        adminForm = helpers.AdminForm(
            form,
            list(self.get_fieldsets(request, obj)),
            # Clear prepopulated fields on a view-only form to avoid a crash.
            self.get_prepopulated_fields(request, obj) if add or self.has_change_permission(request, obj) else {},
            readonly_fields,
            model_admin=self)

        media = self.media + adminForm.media

        inline_formsets = self.get_inline_formsets(request, formsets, inline_instances, obj)
        for inline_formset in inline_formsets:
            media = media + inline_formset.media

        if add:
            title = _('Add %s')
        elif self.has_change_permission(request, obj):
            title = _('Change %s')
        else:
            title = _('View %s')
        cl = self.get_cl(request)
        model_name = '_'.join(str(cl.opts).split('.'))
        context = {
            **self.admin_site.each_context(request),
            'title': title % opts.verbose_name,
            'adminform': adminForm,
            'model_name': model_name,
            # 'open_addPage':[i[0] for i in self.open_addPage],
            # 'open_dict':open_dict,
            'object_id': object_id,
            'original': obj,
            'is_popup': IS_POPUP_VAR in request.POST or IS_POPUP_VAR in request.GET,
            'to_field': to_field,
            'media': media,
            'inline_admin_formsets': inline_formsets,
            'errors': helpers.AdminErrorList(form, formsets),
            'preserved_filters': self.get_preserved_filters(request),
        }

        # Hide the "Save" and "Save and continue" buttons if "Save as New" was
        # previously chosen to prevent the interface from getting confusing.
        if request.method == 'POST' and not form_validated and "_saveasnew" in request.POST:
            context['show_save'] = False
            context['show_save_and_continue'] = False
            # Use the change template instead of the add template.
            add = False

        context.update(extra_context or {})

        return self.render_change_form(request, context, add=add, change=not add, obj=obj, form_url=form_url)


@admin.register(ArtificialfeedingInfo)
class ArtificialfeedingInfoAdmin(admin.ModelAdmin):
    field_name = ArtificialfeedingInfo()._meta.fields
    list_display = ['id','lamb']

    list_filter = []
    exclude_display = ['belong','ele_id']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(weaningInfo)
class weaningInfoAdmin(admin.ModelAdmin):
    field_name = weaningInfo()._meta.fields
    list_display = ['id', 'ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = weaningInfo.objects.all().values('basic_id')
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
            return weaningInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'


@admin.register(LambInfo)
class LambInfo(admin.ModelAdmin):
    field_name = LambInfo()._meta.fields
    list_display = []

    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []

    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'e_breed/change_list_lamb.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

    def get_urls(self):
        from django.urls import path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        return [
            path('', wrap(self.changelist_view), name='%s_%s_changelist' % info),
            path('add/', wrap(self.add_view), name='%s_%s_add' % info),
            path('page/', wrap(self.page_view), name='%s_%s_page' % info),
            path('lambTobasic/', self.lambTobasic, name='%s_%s_page' % info),
            path('autocomplete/', wrap(self.autocomplete_view), name='%s_%s_autocomplete' % info),
            path('<path:object_id>/history/', wrap(self.history_view), name='%s_%s_history' % info),
            path('<path:object_id>/delete/', wrap(self.delete_view), name='%s_%s_delete' % info),
            path('<path:object_id>/change/', wrap(self.change_view), name='%s_%s_change' % info),
            # For backwards compatibility (was the change url before 1.9)
            path('<path:object_id>/', wrap(RedirectView.as_view(
                pattern_name='%s:%s_%s_change' % ((self.admin_site.name,) + info)
            ))),
        ]

    def lambTobasic(self, request):
        lamb_ids = request.GET.getlist('s')
        for lamb_id in lamb_ids:
            from .models import LambInfo
            lamb = LambInfo.objects.filter(id=int(lamb_id)).first()
            dict = {}
            for i in BasicInfo._meta.fields:
                dict[i.name] = eval('lamb.{}'.format(i.name))
            del dict['id']
            BasicInfo.objects.create(**dict)
            LambInfo.objects.filter(id=int(lamb_id)).update(tobasic=True)

        return HttpResponse("ok")
