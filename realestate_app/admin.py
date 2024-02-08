from django.contrib import admin
from .models import Land, Property, Property_type, Image, Video
from django import forms
# Register your models here.
class LandAdmin(admin.ModelAdmin):
    pass

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the 'property' and 'land' fields as optional
        self.fields['property'].required = False
        self.fields['land'].required = False

class ImageAdmin(admin.ModelAdmin):
    form = ImageForm

admin.site.register(Land)
admin.site.register(Property)
admin.site.register(Property_type)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video)