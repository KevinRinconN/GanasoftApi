from django.contrib import admin
from bovine.models import Bovine

@admin.register(Bovine)
class bovineAdmin(admin.ModelAdmin):
    list_display = ['id', 'distinctiveTrait', 'breed', 'is_female', 'dateOfBirth']
