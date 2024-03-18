# custom_filters.py
from django import template

register = template.Library()

@register.filter
def slice_by_words(value, num_words):
    """
    Slices a string by words.
    """
    words = value.split()
    return ' '.join(words[:num_words])
