from django.contrib import admin

from bakeryProject.bakery_main.models import BakeryUser, Profile


@admin.register(BakeryUser)
class AdminBakeryUser(admin.ModelAdmin):
    pass


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
