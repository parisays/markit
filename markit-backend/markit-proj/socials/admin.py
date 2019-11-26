from django.contrib import admin
from .models import SocialAccount, SocialApp

class SocialAppAdmin(admin.ModelAdmin):
    """
    Custom social app admin page.
    """
    list_display = ('id', 'name', 'provider',)
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('provider',)
    search_fields = ('provider',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('name', 'provider', 'clientId', 'secret',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'provider', 'clientId', 'secret',)}
        ),
    )

class SocialAccountAdmin(admin.ModelAdmin):
    """
    Custom social app admin page.
    """
    list_display = ('id', 'app', 'calendar', 'provider',)
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('provider', 'calendar',)
    search_fields = ('provider', 'calendar',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('app', 'calendar', 'provider', 'token', 'tokenSecret', 'expireDate',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('app', 'calendar', 'provider',)}
        ),
    )

admin.site.register(SocialApp, SocialAppAdmin)
admin.site.register(SocialAccount, SocialAccountAdmin)
