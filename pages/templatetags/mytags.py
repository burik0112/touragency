from django import template

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path
    url = url.split('/')
    url[1] = lang
    url = '/'.join(url)
    return url
