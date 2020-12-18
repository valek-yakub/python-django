from django import template

register = template.Library()


@register.filter(name="range")
def range(start, stop):
    return range(start, stop)
