from django.contrib import admin

# Register your models here.
from .models import UserDetails , UserActivityPeriod
#  ActivityPeriod ,
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(UserActivityPeriod)

