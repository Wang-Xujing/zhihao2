from django.contrib import admin
from . models import *
from apps import *
from .models import *
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

IS_POPUP_VAR = '_popup'
TO_FIELD_VAR = '_to_field'
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    field_name = Inventory()._meta.fields
    list_display = ['maker']
    list_filter = []
    exclude_display = ['belong','id']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
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
    def _changeform_view(self, request, object_id, form_url, extra_context):
        ##########

        from apps.h_store.models import Vaccine_in
        from apps.supply.models import v_suppliersInfo
        from apps.supply.models import f_suppliersInfo
        from apps.basic.models import BasicInfo
        import datetime
        request_copy = request.POST.copy()
        if request.method == "POST":
            ####疫苗药物厂商
            try:
                id_maker = 'maker_id'
                if 'drug_id' in request_copy:
                    id_vaccine = 'vac_maker'
                if len(request_copy['many-supply_v_suppliersinfo']) > 0:
                    request_copy[id_maker] = request_copy['many-supply_v_suppliersinfo'][:-1]
                elif len(request_copy['supply_v_suppliersinfo']) > 0:
                    request_copy[id_maker] = str(v_suppliersInfo.objects.filter(supplier_name=request_copy['supply_v_suppliersinfo']).values('id').first()['id'])
                    print('ok')
                else:
                    pass
            except MultiValueDictKeyError:
                pass
            v_name=request_copy['v_name']
            maker=request_copy['maker_id']
            type=request_copy['type']
            inventory=Inventory.objects.filter(goods=v_name,maker_id=maker,type=type).first()
            if inventory :
                request_copy['keep_amount']=str(inventory.quantity)
            else:
                request_copy['keep_amount']='0'

            #request_copy['keep_amount']=

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
        if request.method == 'POST':
            belong = request.POST.get('belong')
            v_name = request.POST.get('v_name')
            type_in = request.POST.get('type')
            manu = request.POST.get('maker_id')
            in_amount = request.POST.get('in_amount')
            f_date = '-'.join(request.POST.get('f_date').split('/'))
            operation = request.POST.get('operation')
            name_list = Inventory.objects.values_list('goods', flat=True)
            if v_name not in name_list:
                Inventory.objects.create(belong=belong, goods=v_name, type=type_in, maker_id=manu,quantity=in_amount, f_date=f_date, operation=operation)
            else:
                inventory = Inventory.objects.filter(goods=v_name)
                m_list = inventory.values_list('maker_id', flat=True)
                if int(manu) not in m_list:
                    Inventory.objects.create(belong=belong, goods=v_name, type=type_in, maker_id=manu, quantity=in_amount, f_date=f_date, operation=operation)
        ####
        request.POST=request_copy
        print(request.POST)
        if request.method == 'POST':
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
        cl=self.get_cl(request)
        model_name = '_'.join(str(cl.opts).split('.'))
        context = {
            **self.admin_site.each_context(request),
            'title': title % opts.verbose_name,
            'adminform': adminForm,
            'model_name':model_name,
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
    def _changeform_view(self, request, object_id, form_url, extra_context):
        ##########

        from apps.h_store.models import Vaccine_in
        from apps.supply.models import v_suppliersInfo
        from apps.supply.models import f_suppliersInfo
        from apps.basic.models import BasicInfo
        import datetime
        request_copy = request.POST.copy()
        if request.method == "POST":
            try:
                id_maker = 'maker_id'
                if len(request_copy['many-supply_f_suppliersinfo']) > 0:
                    request_copy[id_maker] = request_copy['many-supply_f_suppliersinfo'][:-1]
                elif len(request_copy['supply_f_suppliersinfo']) > 0:
                    request_copy[id_maker] = str(f_suppliersInfo.objects.filter(supplier_name=request_copy['supply_f_suppliersinfo']).values('id').first()['id'])
                    print('ok')
                else:
                    pass
            except MultiValueDictKeyError:
                pass
            f_name = request_copy['f_name']
            maker = request_copy['maker_id']
            type = request_copy['type']
            inventory = Inventory.objects.filter(goods=f_name, maker_id=maker, type=type).first()
            if inventory:
                request_copy['keep_amount'] = str(inventory.quantity)
            else:
                request_copy['keep_amount'] = '0'
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
        if request.method == 'POST':
            belong = request.POST.get('belong')
            f_name = request.POST.get('f_name')
            type = request.POST.get('type')
            quantity = request.POST.get('quantity')
            FI = request.POST.get('maker_id')
            f_date = '-'.join(request.POST.get('f_date').split('/'))
            operation = request.POST.get('operation')
            name_list = Inventory.objects.values_list('goods', flat=True)
            if f_name not in name_list:
                Inventory.objects.create(belong=belong, goods=f_name, type=type, maker_id=FI,quantity=quantity, f_date=f_date, operation=operation)
            else:
                inventory = Inventory.objects.filter(goods=f_name)
                m_list = inventory.values_list('maker_id', flat=True)
                if int(FI) not in m_list:
                    Inventory.objects.create(belong=belong, goods=f_name, type=type, maker_id=FI,
                                             quantity=quantity, f_date=f_date, operation=operation)

        ####

        if request.method == 'POST':
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
        cl=self.get_cl(request)
        model_name = '_'.join(str(cl.opts).split('.'))
        context = {
            **self.admin_site.each_context(request),
            'title': title % opts.verbose_name,
            'adminform': adminForm,
            'model_name':model_name,
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


