from django import template
from blog_app.models import Category

register = template.Library()

@register.inclusion_tag("blog_app/menu_tpl.html")
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return  {"categories": categories, "menu_class": menu_class}