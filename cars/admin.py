from django.contrib import admin
from django.utils.html import format_html
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'model', 'color', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('thumbnail', 'car_title', 'model')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'model')
    list_filter = ('car_title', 'model')

admin.site.register(Car, CarAdmin)
