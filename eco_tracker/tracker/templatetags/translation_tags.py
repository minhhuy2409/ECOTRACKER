from django import template

register = template.Library()

@register.filter
def translate_key(dictionary, key):
    """
    Looks up a translation key in the given dictionary.
    If the key doesn't exist, returns the original key.
    """
    if not dictionary or not key:
        return key
    
    key_str = str(key).strip()
    return dictionary.get(key_str, key_str)
