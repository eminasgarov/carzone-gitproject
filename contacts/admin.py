from django.contrib import admin
from contacts.models import Contact, Email

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'car_title', 'city')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'subject')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'email', 'subject')
    list_per_page = 25

admin.site.register(Email, EmailAdmin)