from django.contrib import admin
from .models import CustomerLocation

@admin.register(CustomerLocation)
class CustomerLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'country', 'latitude', 'longitude', 'date_added')
    list_filter = ('country', 'city')
    search_fields = ('user__username', 'address', 'city', 'country')
    readonly_fields = ('latitude', 'longitude', 'date_added')
