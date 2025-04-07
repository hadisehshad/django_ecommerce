from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Testimonial)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", "feedback", "rating", "image", "is_active")
    search_fields = ("user", "is_active")
