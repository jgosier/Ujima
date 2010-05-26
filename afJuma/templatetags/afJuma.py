from django import template
from django.template.defaultfilters import stringfilter
import re
register = template.Library()
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.utils.translation import ungettext, ugettext as _
@register.filter
@stringfilter
def mil(value):
    
    value=float(value)
    new_value = value 
    return ungettext('%(value).1f million', '%(value).1f million', new_value) % {'value': new_value}