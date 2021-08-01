from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

from apps import *
from django.http import HttpResponse
# Register your models here.

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
from reportlab.pdfgen import canvas
from django.utils.translation import gettext as _, gettext_lazy
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm,inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
###
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image


class IncorrectLookupParameters(Exception):
    pass
@admin.register(BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    field_name = BasicInfo()._meta.fields
    list_display = ['id','xipu']
    ordering = ('-f_date',)
    list_filter = ['ele_num','house_name','hurdle_name']
    exclude_display = ['belong','manu_info_id','house_id','hurdle_id']
    exclude_filter = []
    search_fields = []
    change_list_template_page = 'test_change_list.html'
    change_list_template_ewe = 'page/test_change_list_ewe.html'
    change_list_template_ram = 'page/test_change_list_ram.html'
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    list_display.remove('change')
    change_list_template = 'basic/change_list_zhu_basic.html'
    def show(self,request):
        id=request.GET.get('id')
        return HttpResponse(id)
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
            path('ewe/', wrap(self.ewe_view), name='%s_%s_page' % info),
            path('ram/', wrap(self.ram_view), name='%s_%s_page' % info),
            path('autocomplete/', wrap(self.autocomplete_view), name='%s_%s_autocomplete' % info),
            path('<path:object_id>/history/', wrap(self.history_view), name='%s_%s_history' % info),
            path('<path:object_id>/delete/', wrap(self.delete_view), name='%s_%s_delete' % info),
            path('<path:object_id>/change/', wrap(self.change_view), name='%s_%s_change' % info),
            # For backwards compatibility (was the change url before 1.9)
            path('<path:object_id>/', wrap(RedirectView.as_view(
                pattern_name='%s:%s_%s_change' % ((self.admin_site.name,) + info)
            ))),
        ]
    def ewe_view(self, request, extra_context=None):
        """
        The 'change list' admin view for this model.
        """
        from django.contrib.admin.views.main import ERROR_FLAG
        opts = self.model._meta
        app_label = opts.app_label
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied

        try:
            cl = self.get_changelist_instance(request)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
            if ERROR_FLAG in request.GET:
                return SimpleTemplateResponse('admin/invalid_setup.html', {
                    'title': _('Database error'),
                })
            return HttpResponseRedirect(request.path + '?' + ERROR_FLAG + '=1')

        # If the request was POSTed, this might be a bulk action or a bulk
        # edit. Try to look up an action or confirmation first, but if this
        # isn't an action the POST will fall through to the bulk edit check,
        # below.
        action_failed = False
        selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
        ##############################
        actions = None
        # Actions with no confirmation
        if (actions and request.method == 'POST' and
                'index' in request.POST and '_save' not in request.POST):
            if selected:
                response = self.response_action(request, queryset=cl.get_queryset(request))
                if response:
                    return response
                else:
                    action_failed = True
            else:
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                self.message_user(request, msg, messages.WARNING)
                action_failed = True

        # Actions with confirmation
        if (actions and request.method == 'POST' and
                helpers.ACTION_CHECKBOX_NAME in request.POST and
                'index' not in request.POST and '_save' not in request.POST):
            if selected:
                response = self.response_action(request, queryset=cl.get_queryset(request))
                if response:
                    return response
                else:
                    action_failed = True

        if action_failed:
            # Redirect back to the changelist page to avoid resubmitting the
            # form if the user refreshes the browser or uses the "No, take
            # me back" button on the action confirmation page.
            return HttpResponseRedirect(request.get_full_path())

        # If we're allowing changelist editing, we need to construct a formset
        # for the changelist given all the fields to be edited. Then we'll
        # use the formset to validate/process POSTed data.
        formset = cl.formset = None

        # Handle POSTed bulk-edit data.
        if request.method == 'POST' and cl.list_editable and '_save' in request.POST:
            if not self.has_change_permission(request):
                raise PermissionDenied
            FormSet = self.get_changelist_formset(request)
            modified_objects = self._get_list_editable_queryset(request, FormSet.get_default_prefix())
            formset = cl.formset = FormSet(request.POST, request.FILES, queryset=modified_objects)
            if formset.is_valid():
                changecount = 0
                for form in formset.forms:
                    if form.has_changed():
                        obj = self.save_form(request, form, change=True)
                        self.save_model(request, obj, form, change=True)
                        self.save_related(request, form, formsets=[], change=True)
                        change_msg = self.construct_change_message(request, form, None)
                        self.log_change(request, obj, change_msg)
                        changecount += 1

                if changecount:
                    msg = ngettext(
                        "%(count)s %(name)s was changed successfully.",
                        "%(count)s %(name)s were changed successfully.",
                        changecount
                    ) % {
                              'count': changecount,
                              'name': model_ngettext(opts, changecount),
                          }
                    self.message_user(request, msg, messages.SUCCESS)

                return HttpResponseRedirect(request.get_full_path())

        # Handle GET -- construct a formset for display.
        elif cl.list_editable and self.has_change_permission(request):
            FormSet = self.get_changelist_formset(request)
            formset = cl.formset = FormSet(queryset=cl.result_list)

        # Build the list of media to be used by the formset.
        if formset:
            media = self.media + formset.media
        else:
            media = self.media

        # Build the action form and populate it with available actions.
        ###############
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_page_action_choices(request)
            media += action_form.media
        else:
            action_form = None

        selection_note_all = ngettext(
            '%(total_count)s selected',
            'All %(total_count)s selected',
            cl.result_count
        )
        ########
        model_label = '_'.join(str(cl.opts).split('.'))
        context = {
            'model_label': model_label,
            **self.admin_site.each_context(request),
            'module_name': str(opts.verbose_name_plural),
            'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
            'selection_note_all': selection_note_all % {'total_count': cl.result_count},
            'title': cl.title,
            'is_popup': cl.is_popup,
            'to_field': cl.to_field,
            'cl': cl,
            'media': media,
            'has_add_permission': self.has_add_permission(request),
            'opts': cl.opts,
            'action_form': action_form,
            'actions_on_top': self.actions_on_top,
            'actions_on_bottom': self.actions_on_bottom,
            'actions_selection_counter': self.actions_selection_counter,
            'preserved_filters': self.get_preserved_filters(request),
            **(extra_context or {}),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(request, self.change_list_template_ewe or [
            'admin/%s/%s/change_list.html' % (app_label, opts.model_name),
            'admin/%s/change_list.html' % app_label,
            'admin/change_list.html'
        ], context)
    def ram_view(self, request, extra_context=None):
        """
        The 'change list' admin view for this model.
        """
        from django.contrib.admin.views.main import ERROR_FLAG
        opts = self.model._meta
        app_label = opts.app_label
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied

        try:
            cl = self.get_changelist_instance(request)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
            if ERROR_FLAG in request.GET:
                return SimpleTemplateResponse('admin/invalid_setup.html', {
                    'title': _('Database error'),
                })
            return HttpResponseRedirect(request.path + '?' + ERROR_FLAG + '=1')

        # If the request was POSTed, this might be a bulk action or a bulk
        # edit. Try to look up an action or confirmation first, but if this
        # isn't an action the POST will fall through to the bulk edit check,
        # below.
        action_failed = False
        selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
        ##############################
        actions = None
        # Actions with no confirmation
        if (actions and request.method == 'POST' and
                'index' in request.POST and '_save' not in request.POST):
            if selected:
                response = self.response_action(request, queryset=cl.get_queryset(request))
                if response:
                    return response
                else:
                    action_failed = True
            else:
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                self.message_user(request, msg, messages.WARNING)
                action_failed = True

        # Actions with confirmation
        if (actions and request.method == 'POST' and
                helpers.ACTION_CHECKBOX_NAME in request.POST and
                'index' not in request.POST and '_save' not in request.POST):
            if selected:
                response = self.response_action(request, queryset=cl.get_queryset(request))
                if response:
                    return response
                else:
                    action_failed = True

        if action_failed:
            # Redirect back to the changelist page to avoid resubmitting the
            # form if the user refreshes the browser or uses the "No, take
            # me back" button on the action confirmation page.
            return HttpResponseRedirect(request.get_full_path())

        # If we're allowing changelist editing, we need to construct a formset
        # for the changelist given all the fields to be edited. Then we'll
        # use the formset to validate/process POSTed data.
        formset = cl.formset = None

        # Handle POSTed bulk-edit data.
        if request.method == 'POST' and cl.list_editable and '_save' in request.POST:
            if not self.has_change_permission(request):
                raise PermissionDenied
            FormSet = self.get_changelist_formset(request)
            modified_objects = self._get_list_editable_queryset(request, FormSet.get_default_prefix())
            formset = cl.formset = FormSet(request.POST, request.FILES, queryset=modified_objects)
            if formset.is_valid():
                changecount = 0
                for form in formset.forms:
                    if form.has_changed():
                        obj = self.save_form(request, form, change=True)
                        self.save_model(request, obj, form, change=True)
                        self.save_related(request, form, formsets=[], change=True)
                        change_msg = self.construct_change_message(request, form, None)
                        self.log_change(request, obj, change_msg)
                        changecount += 1

                if changecount:
                    msg = ngettext(
                        "%(count)s %(name)s was changed successfully.",
                        "%(count)s %(name)s were changed successfully.",
                        changecount
                    ) % {
                              'count': changecount,
                              'name': model_ngettext(opts, changecount),
                          }
                    self.message_user(request, msg, messages.SUCCESS)

                return HttpResponseRedirect(request.get_full_path())

        # Handle GET -- construct a formset for display.
        elif cl.list_editable and self.has_change_permission(request):
            FormSet = self.get_changelist_formset(request)
            formset = cl.formset = FormSet(queryset=cl.result_list)

        # Build the list of media to be used by the formset.
        if formset:
            media = self.media + formset.media
        else:
            media = self.media

        # Build the action form and populate it with available actions.
        ###############
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_page_action_choices(request)
            media += action_form.media
        else:
            action_form = None

        selection_note_all = ngettext(
            '%(total_count)s selected',
            'All %(total_count)s selected',
            cl.result_count
        )
        ########
        model_label = '_'.join(str(cl.opts).split('.'))
        context = {
            'model_label': model_label,
            **self.admin_site.each_context(request),
            'module_name': str(opts.verbose_name_plural),
            'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
            'selection_note_all': selection_note_all % {'total_count': cl.result_count},
            'title': cl.title,
            'is_popup': cl.is_popup,
            'to_field': cl.to_field,
            'cl': cl,
            'media': media,
            'has_add_permission': self.has_add_permission(request),
            'opts': cl.opts,
            'action_form': action_form,
            'actions_on_top': self.actions_on_top,
            'actions_on_bottom': self.actions_on_bottom,
            'actions_selection_counter': self.actions_selection_counter,
            'preserved_filters': self.get_preserved_filters(request),
            **(extra_context or {}),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(request, self.change_list_template_ram or [
            'admin/%s/%s/change_list.html' % (app_label, opts.model_name),
            'admin/%s/change_list.html' % app_label,
            'admin/change_list.html'
        ], context)

    #导出系谱档案
    # def genTaskPDF(self):
    #     story = []
    #
    #     # 首页内容
    #     story.append(Spacer(1, 20 * mm))
    #     img = Image('/xxx/xxx.png')
    #     img.drawHeight = 20 * mm
    #     img.drawWidth = 40 * mm
    #     img.hAlign = TA_LEFT
    #     story.append(img)
    #     story.append(Spacer(1, 10 * mm))
    #     story.append(Paragraph("测试报告", self.title_style))
    #     story.append(Spacer(1, 20 * mm))
    #     story.append(Paragraph("Test Report of XXX", self.sub_title_style))
    #     story.append(Spacer(1, 45 * mm))
    #     # story.append(Paragraph("报告编号：" + home_data['report_code'], self.content_style))
    #     # story.append(Paragraph("计划名称：" + home_data['task_name'], self.content_style))
    #     # story.append(Paragraph("报告日期：" + home_data['report_date'], self.content_style))
    #     # story.append(Paragraph(" 负责人：" + home_data['report_creator'], self.content_style))
    #     story.append(Spacer(1, 55 * mm))
    #     story.append(Paragraph("内部文档，请勿外传", self.foot_style))
    #     story.append(PageBreak())
    #
    #     # 表格允许单元格内容自动换行格式设置
    #     stylesheet = getSampleStyleSheet()
    #     body_style = stylesheet["BodyText"]
    #     body_style.wordWrap = 'CJK'
    #     body_style.fontName = 'ping'
    #     body_style.fontSize = 12
    #
    #     # 测试计划
    #     story.append(Paragraph("测试计划", self.table_title_style))
    #     story.append(Spacer(1, 3 * mm))
    #     # task_table = Table(task_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
    #     # story.append(task_table)
    #
    #     story.append(Spacer(1, 10 * mm))
    #
    #     # 基础参数
    #     story.append(Paragraph("基础参数", self.sub_table_style))
    #     # basic_table = Table(basic_data, colWidths=[25 * mm, 61 * mm, 25 * mm, 55 * mm], rowHeights=12 * mm,style=self.basic_style)
    #     # story.append(basic_table)
    #
    #     story.append(Spacer(1, 10 * mm))
    #
    #     # 测试用例集
    #     story.append(Paragraph("用例集参数", self.sub_table_style))
    #     # case_set_table = Table(case_set_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm,style=self.common_style)
    #     # story.append(case_set_table)
    #
    #     # story.append(PageBreak())
    #     story.append(Spacer(1, 15 * mm))
    #
    #     # 失败用例--使用可以自动换行的方式需要data里都是str类型的才OK
    #     story.append(Paragraph("失败用例", self.table_title_style))
    #     story.append(Spacer(1, 3 * mm))
    #     # para_fail_case_data = [[Paragraph(cell, body_style) for cell in row] for row in fail_case_data]
    #     # fail_case_table = Table(para_fail_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
    #     # fail_case_table.setStyle(self.common_style)
    #     # story.append(fail_case_table)
    #
    #     story.append(Spacer(1, 15 * mm))
    #
    #     # 基础用例（P0）
    #     story.append(Paragraph("基础用例（P0）", self.table_title_style))
    #     story.append(Spacer(1, 3 * mm))
    #     # para_p0_case_data = [[Paragraph(cell, body_style) for cell in row] for row in p0_case_data]
    #     # p0_case_table = Table(para_p0_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
    #     # p0_case_table.setStyle(self.common_style)
    #     # story.append(p0_case_table)
    #
    #     doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
    #                             leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
    #
    #     doc.build(story)
    #     return
    # def export_to_pdf(self, request, queryset):
    #
    #     for obj in queryset:  # 遍历选择的对象列表
    #         print(obj.ele_num)
    #         response = HttpResponse(content_type='application/pdf')
    #         response[
    #             'Content-Disposition'] = f'attachment; filename={obj.ele_num}.pdf'.encode(
    #             'utf-8')  # 定义响应数据格式
    #
    #         # Create the PDF object, using the response object as its "file."
    #         p = canvas.Canvas(response)
    #         p.setPageSize((16 * inch, 22 * inch))
    #         textobj = p.beginText()
    #         textobj.setTextOrigin(inch, 20 * inch)
    #         textobj.textLines('''
    #                     This is the scanning report of %s.
    #                     ''' )
    #         textobj.textLines('''
    #                     Date: %s
    #                     ''')
    #         # for line in range:
    #         #     textobj.textLine(line.strip())
    #         p.drawText(textobj)
    #         # Draw things on the PDF. Here's where the PDF generation happens.
    #         # See the ReportLab documentation for the full list of functionality.
    #         # p.drawString(0, 0, "Hello world.")
    #         # story=self.genTaskPDF()
    #         # p.drawBoundary(1,1,1)
    #
    #         # Close the PDF object cleanly, and we're done.
    #         p.showPage()
    #         p.save()
    #     return response



    # export_to_pdf.allowed_permissions = ('export',)
    # export_to_pdf.short_description = gettext_lazy("导出系谱档案")
    #
    # actions = [export_to_pdf]
@admin.register(manuInfo)
class manuInfoAdmin(admin.ModelAdmin):

    field_name = manuInfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name,list_display,exclude_display,list_filter,exclude_filter,search_fields)
    ordering = ('id',)
    add_form_template = 'test.html'
    change_form_template = 'test.html'
    change_list_template = 'change_list_zhu.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(elechangeInfo)
class elechangeInfoAdmin(admin.ModelAdmin):

    field_name = elechangeInfo()._meta.fields
    list_display = []
    list_filter = []
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name,list_display,exclude_display,list_filter,exclude_filter,search_fields)
    ordering = ('id',)
@admin.register(BreederconditionInfo)
class BreederconditionInfoAdmin(admin.ModelAdmin):

    field_name = BreederconditionInfo()._meta.fields
    list_display = ['ele_id']
    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = BreederconditionInfo.objects.all().values('basic_id')
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
            return BreederconditionInfo.objects.filter(basic_id=basic['id']).all()
    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ##不显示字段
    list_display.remove('age')
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
class BreederAdmin(ImportExportModelAdmin):
    pass
@admin.register(cutInfo)
class cutInfoAdmin(admin.ModelAdmin):
    field_name = cutInfo()._meta.fields
    list_display = ['house']
    class pidFilter(admin.SimpleListFilter):
        title = "棚"
        parameter_name = 'pid'

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
            h_id=[i['id'] for i in list(house)]
            h_id.append(peng['id'])
            return cutInfo.objects.filter(house_id__in=h_id).all()
    class HouseFilter(admin.SimpleListFilter):
        title = "棚"
        parameter_name = 'house_id'

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
            h_id=[i['id'] for i in list(house)]
            h_id.append(peng['id'])
            return cutInfo.objects.filter(house_id__in=h_id).all()
    list_filter = [pidFilter]
    exclude_display = ['belong','house_id']
    exclude_filter = []
    search_fields = []
    doit(field_name,list_display,exclude_display,list_filter,exclude_filter,search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(sportsInfo)
class sportsInfoAdmin(admin.ModelAdmin):

    field_name = sportsInfo()._meta.fields
    list_display = ['ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = sportsInfo.objects.all().values('basic_id')
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
            return sportsInfo.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]
    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name,list_display,exclude_display,list_filter,exclude_filter,search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
@admin.register(productivityInfo)
class productivityInfoAdmin(admin.ModelAdmin):

    field_name = productivityInfo()._meta.fields
    list_display = ['ele_id']
    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = productivityInfo.objects.all().values('basic_id')
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
            return productivityInfo.objects.filter(basic_id=basic['id']).all()
    list_filter = [eleFilter]

    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
@admin.register(milkperformance)
class milkperformanceAdmin(admin.ModelAdmin):
    field_name = milkperformance()._meta.fields
    list_display = ['ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = milkperformance.objects.all().values('basic_id')
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
            return milkperformance.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]

    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'

@admin.register(skinperformance)
class skinperformanceAdmin(admin.ModelAdmin):
    field_name = skinperformance()._meta.fields
    list_display = ['ele_id']

    class eleFilter(admin.SimpleListFilter):
        title = "电子耳号"
        parameter_name = 'basic_id'

        def lookups(self, request, model_admin):
            params = skinperformance.objects.all().values('basic_id')
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
            return skinperformance.objects.filter(basic_id=basic['id']).all()

    list_filter = [eleFilter]

    exclude_display = ['belong']
    exclude_filter = []
    search_fields = []
    doit(field_name, list_display, exclude_display, list_filter, exclude_filter, search_fields)
    ordering = ('id',)
    change_list_template = 'change_list_zhu.html'
    add_form_template = 'test.html'
    change_list_template_page = 'test_change_list.html'
