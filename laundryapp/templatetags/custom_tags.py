from django import template
from laundryapp.models import *

register = template.Library()

@register.simple_tag
def price_cal(qty, price):
    return int(qty) * float(price)

@register.simple_tag
def total_price_cal(qty1, price1, qty2, price2, qty3, price3):
    return ((int(qty1) * float(price1)) + (int(qty2) * float(price2)) + (int(qty3) * float(price3)))

@register.simple_tag
def total_qty(qty1, qty2, qty3, qty4):
    return int(qty1) + int(qty3) + int(qty2) + int(qty4)

@register.simple_tag
def laundry_count(create_date, status):
    if status == "Total":
        laundry_obj = Laundry.objects.filter(creationdate__date=create_date)
        return laundry_obj.count()
    else:
        laundry_obj = Laundry.objects.filter(creationdate__date=create_date, status=status)
        return laundry_obj.count()
