
from django import template

register = template.Library()

@register.filter(name='displayName')
def displayName(value, arg):
    return eval('value.get_'+arg+'_display()')

@register.filter
def db_star(value):
    return value/10
