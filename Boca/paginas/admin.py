from django.contrib import admin

# Register your models here.
from .models import contest,option

admin.site.register(contest)
admin.site.register(option)