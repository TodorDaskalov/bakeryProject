from django.contrib import admin
from bakeryProject.bakery_main.models import BakeryUser, Profile


@admin.register(BakeryUser)
class AdminBakeryUser(admin.ModelAdmin):
    list_display = ('email', 'is_staff')
    ordering = ('email', 'is_staff')
    list_filter = ('email', 'is_staff')
    search_fields = ('email', 'is_staff')


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    ordering = ('user', 'first_name', 'last_name', 'phone_number')
    list_filter = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('first_name', 'last_name', 'phone_number')


admin.site.site_header = 'Bakery Admin'
admin.site.site_title = 'Bakery Admin Panel'
