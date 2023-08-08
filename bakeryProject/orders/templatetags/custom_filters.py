from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    return float(value) * float(arg)


@register.filter(name='custom_time_format')
def custom_time_format(value):
    try:
        hour, minute = value.split(':')
        return f'{hour}:{minute}'
    except ValueError:
        return value
