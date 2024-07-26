from django.contrib import admin

from .models import User, Token, Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ["_id", "nameRU", "nameEN"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["_id", "email"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Token)
