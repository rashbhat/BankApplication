from django.contrib import admin
from .models import BankDetails,UserDetails
# Register your models here.
admin.site.register(BankDetails)
admin.site.register(UserDetails)
