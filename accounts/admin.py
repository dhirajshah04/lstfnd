from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth', 'phone', 'gender', 'country',
                    'city', 'website', 'photo']

admin.site.register(Profile, ProfileAdmin)