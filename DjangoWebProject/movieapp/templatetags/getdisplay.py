
from django import template

register = template.Library()

@register.filter(name='displayName')
def displayName(value, arg):
    return eval('value.get_'+arg+'_display()')

@register.filter
def db_star(value):
    return value/10

@register.filter
def setEndClass(value,count):
    if value % int(count) ==0 :
        return "class=end"
