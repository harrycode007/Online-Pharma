from django.contrib import admin
from .models import Registration
from .models import Contact, MedicineOrdered, Contactlogin

# All the models used are registered here. The data stored in these modules can be accessed via the admin dashboard.
admin.site.register(Registration)
admin.site.register(Contact)
admin.site.register(MedicineOrdered)