from .models import Booking


def get_clinics(booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return booking