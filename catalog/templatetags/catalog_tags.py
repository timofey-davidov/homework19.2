from django import template
from django.conf import settings

register = template.Library()
@register.filter
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'

@register.simple_tag
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'
