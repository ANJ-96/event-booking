from django.contrib import admin
from .models import Event, Booking

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0  # Don't show empty rows
    readonly_fields = ['name', 'email', 'num_seats', 'booked_at']

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'capacity', 'seats_left', 'status']
    inlines = [BookingInline]

    def status(self, obj):
        return "Sold Out" if obj.seats_left() == 0 else "Available"

    status.short_description = "Status"
    status.admin_order_field = "capacity"

admin.site.register(Event, EventAdmin)
admin.site.register(Booking)
