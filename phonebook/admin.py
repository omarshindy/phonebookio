from django.contrib import admin
from phonebook.models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_name', 'phone_number', 'phone_type')