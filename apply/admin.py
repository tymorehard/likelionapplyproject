from django.contrib import admin
from .models import Apply
from account.models import CustomUser

# Register your models here.
admin.site.register(Apply)
admin.site.register(CustomUser)