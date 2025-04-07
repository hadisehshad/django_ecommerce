from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)