from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(positions)
admin.site.register(services)
admin.site.register(doctors)
admin.site.register(animals)
admin.site.register(status)
admin.site.register(heal)