from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user")


@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "is_staff", "date_joined")
    search_fields = ("phone_number", "is_staff", "date_joined")


@admin.register(OTPCode)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created_at")
    search_fields = ("phone_number", "created_at")


@admin.register(ShoppingCart)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid", "created_at")
    search_fields = ("is_paid", "created_at")


@admin.register(CartItems)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("cart", "quantity", "product")


admin.site.register(Notification)
