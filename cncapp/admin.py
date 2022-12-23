from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Inventory)
admin.site.register(Pharmacist)
admin.site.register(Patient)
admin.site.register(Driver)
admin.site.register(Ambulance)
admin.site.register(Datashare)
admin.site.register(AmbulnceDatashare)
admin.site.register(DocDatashare)
admin.site.register(Booking)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(ShippingAddress)
admin.site.register(Pathologist)
admin.site.register(PathologyBooking)
admin.site.register(PathologyDatashare)