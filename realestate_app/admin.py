from django.contrib import admin
from .models import Land, Property, Property_type, Image
# Register your models here.
class LandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Land)
admin.site.register(Property)
admin.site.register(Property_type)
admin.site.register(Image)