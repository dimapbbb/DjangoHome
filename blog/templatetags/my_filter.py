from django import template


register = template.Library()


@register.filter()
def mod_path(image):
    if image:
        res = f"/media/{image}"
        return res
    return "#"
