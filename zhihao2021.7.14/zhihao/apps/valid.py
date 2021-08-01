from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valid_null(value):
    print(value)
    print('ok')
    if not value or value=="":
        raise ValidationError(
            _('%(value)s不能为空'),
            params={'value',value},
        )
    if value:
        if value>9:
            raise ValidationError(
                _('%(value)s不能为空'),
                params={'value',value},
            )

def valid_boolean(value):
    print(value)
    print('ok')
    if not value:
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