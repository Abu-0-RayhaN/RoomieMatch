from django.contrib import admin

# Register your models here.
from .models import Property
from .models import District,PropertyImage
admin.site.register(PropertyImage)
admin.site.register(Property)
admin.site.register(District)