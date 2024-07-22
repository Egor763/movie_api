from django.contrib import admin

from .models import User, Movie, Token


class MovieAdmin(admin.ModelAdmin):
    list_display = ["_id", "name"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["_id", "name", "email"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Token)
