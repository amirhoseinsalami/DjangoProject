from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def days_remaining(due_date):
    if not due_date:
        return None
    delta = due_date.day - timezone.now().day
    return delta

