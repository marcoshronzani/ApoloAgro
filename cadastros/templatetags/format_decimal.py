from django import template

register = template.Library()


@register.filter(name='format_decimal')
def format_decimal(value):
    try:
        value = format(value)
    except:
        pass

    return value