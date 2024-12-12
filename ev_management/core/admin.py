from django.contrib import admin
from .models import User, EVCenter, Booking, Payment

admin.site.register(User)
admin.site.register(EVCenter)
admin.site.register(Booking)
admin.site.register(Payment)
