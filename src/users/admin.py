from django.contrib import admin

from .models import User


@admin.register(User)
class AUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role')
    list_display_links = ('email', 'username')
    search_fields = ('email', 'username')
    exclude = ('password', 'groups', 'last_login')
    list_filter = ('role', )
