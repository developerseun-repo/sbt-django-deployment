from django import template

register = template.Library()

#One way to build a custom template
# def cut(value, arg):
#     """
#     This cuts out all values of "arg" from the string!
#     """

#     return value.replace(arg,'')

# register.filter('cut',cut)


#Other way to build a custom template using decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')