# Packages
from django.contrib import admin

# Modules
from .models import Posts, Followers, Following

# Register your models here.
admin.site.register(Posts)
admin.site.register(Followers)
admin.site.register(Following)
