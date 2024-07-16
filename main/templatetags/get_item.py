from django import template

register = template.Library()

@register.filter()
def get_item(dictionary, key):
    # Отсутствие ошибок KeyError!
    return dictionary.get(key, 'К сожалению, значение не найдено!')
