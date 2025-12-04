from django.contrib import admin

# Register your models here.
from .models import UserAccount, OTP

admin.site.register(UserAccount)
admin.site.register(OTP)
