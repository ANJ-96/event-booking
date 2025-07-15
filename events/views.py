from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Event
from .forms import BookingForm

# 1. Show all events
class EventListView(View):
    def get(self, request):
        events = Event.objects.order_by('date')  # Get all upcoming events
        return render(request, 'events/event_list.html', {'events': events})

# 2. Show single event & booking form
class EventDetailView(View):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)  # Get event by ID
        form = BookingForm()  # Empty form
        return render(request, 'events/event_detail.html', {'event': event, 'form': form})

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        form = BookingForm(request.POST)  # Form filled by user
        if form.is_valid():
            booking = form.save(commit=False)
            if event.seats_left() >= booking.num_seats:
                booking.event = event
                booking.save()
                return redirect('booking_success')  # Show confirmation page
            else:
                form.add_error(None, 'Not enough seats available.')  # Show error
        return render(request, 'events/event_detail.html', {'event': event, 'form': form})

# 3. Booking confirmation page
def booking_success(request):
    return render(request, 'events/booking_success.html')

def booking_success(request):
    return render(request, 'events/booking_success.html')
