from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def doit(field_name,list_display,exclude_display,list_filter,exclude_filter,search_fields):
    list_display.insert(0,'change')
    for i in field_name:
        model_type = str(i.__class__).split('.')[-1][0:-2]
        name = i.name
        if model_type == 'ImageField':
            exclude_filter.append(name)
            continue
        if name not in exclude_display:
            list_display.append(name)
        if name not in exclude_filter and (i.choices or model_type == 'DateField' or model_type == 'DateTimeField'):
            list_filter.append(name)
            exclude_filter.append(name)
        if name not in exclude_filter:
            search_fields.append('='+name)



def valid_null(value):
    print(value)
    print('ok')
    if not value or value=="" or len(value)<2:
        raise ValidationError(
            _('%(value)s不能为空'),
            params={'value',value},
        )
def valid_third(value):
    print(value)
    print('ok')
    n=13
    lenth=len(value)
    if lenth!=n:
        raise ValidationError(
            _('{}是{}位，应该是{}位'.format(value,str(lenth),str(n))),
        )
def valid_ev(value):
    print(value)
    print('ok')
    n=11
    lenth=len(value)
    if lenth!=n:
        raise ValidationError(
            _('{}是{}位，应该是{}位'.format(value,str(lenth),str(n))),
        )
