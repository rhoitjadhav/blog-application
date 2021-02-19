# Packages
from django.contrib import admin

# Modules
from .models import Following, Followers

admin.site.register(Following)
admin.site.register(Followers)
