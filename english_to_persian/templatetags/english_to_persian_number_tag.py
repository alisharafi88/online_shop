from django import template

register = template.Library()


@register.filter
def translate(number):
    english_number = str(number)
    english = '0123456789'
    persian = '۰۱۲۳۴۵۶۷۸۹'

    translation_table = english_number.maketrans(english, persian)

    return english_number.translate(translation_table)
