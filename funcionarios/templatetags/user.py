from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def mostrarUsuario(context):
    return context.request.user.first_name
