from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def seats_left(self):
        booked = sum(booking.num_seats for booking in self.bookings.all())
        return self.capacity - booked


class Booking(models.Model):
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    num_seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
