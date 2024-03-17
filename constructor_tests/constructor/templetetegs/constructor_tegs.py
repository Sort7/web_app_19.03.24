from django import template
from constructor.models import Tests, Categories

# Cоздание простого пользовательского тега
register = template.Library()

@register.simple_tag()
def get_categories():
    return Categories.objects.all()
