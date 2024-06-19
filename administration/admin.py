from django.contrib import admin

from .models import UserProfile, City, State
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(State)
