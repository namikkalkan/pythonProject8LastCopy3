import datetime
from .models import  *

def check_availability(item,check_in,check_out):
    avail_list = []
    booking_list = Order_list.objects.filter(product=item)
    for booking in booking_list:
        if booking.rent_from > check_out or booking.rent_to < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)