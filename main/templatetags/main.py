from django import template
from django.template.defaultfilters import stringfilter
import re
register = template.Library()
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.utils.translation import ungettext, ugettext as _
from Ujima.main.forms import SearchForm





def dict_value(dict,key):
    return dict[key]
def intcomma(value):
    """
    Converts an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    orig = force_unicode(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intcomma(new)
def intword(value):
    """
    Converts a large integer to a friendly text representation. Works best for
    numbers over 1 million. For example, 1000000 becomes '1.0 million', 1200000
    becomes '1.2 million' and '1200000000' becomes '1.2 billion'.
    """
    value=float(value)
    new_value = value / 1000000.0
    return ungettext('%(value).1f million', '%(value).1f million', new_value) % {'value': new_value}
    
@register.filter
@stringfilter
def doll(c):
    """
    Adds a Dollar sign to a currency e.g 4000 becomes $4000
    """
    if c>0:
        #orig= "$%s"%c
        if(float(c)>1000000):
            new=intword(c)
        else:   
            new= intcomma(c)#re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', c)
        return "$%s"%new
    else:
        new= intcomma(c)
        return "-$%s"%(-1*new)
         

@register.filter
@stringfilter
def euro(c):
    """
    Adds an euro sign to euros e.g 4000 becomes 
    """
    if c>0:
        
        if(float(c)<1000000):
            new=intcomma(c)
        else:   
            new= intword(c)#re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', 
        
        return mark_safe("&#8364;%s"%new)
    else:
        new= intcomma(c)
        return mark_safe("-&#8364;%s"%(-1*new))
@register.filter
@stringfilter
def mil(value):
    
    value=float(value)
    new_value = value 
    return ungettext('%(value).1f million', '%(value).1f million', new_value) % {'value': new_value}
class Countries(template.Node):
    def __init__(self,var_name):
        self.var_name=var_name
    def render(self,context):
        from mapping.models import Country
        countries=Country.objects.filter(continent='AF')
        context[self.var_name] = countries
        return ''
@register.tag
def get_countries(parser,token):
    """
    get all countries in the context
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return Countries(var_name)
