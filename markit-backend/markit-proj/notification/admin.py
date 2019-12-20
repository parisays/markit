from django import forms
from django.contrib import admin
from .models import Invitation

class InvitationAdmin(admin.ModelAdmin):
    """
    Custom invitation admin page.
    """
    list_display = ('id', 'calendar', 'invited', 'inviter',)
    list_display_links = ('invited',)
    ordering = ('id', 'calendar', 'invited', 'inviter',)
    list_filter = ('calendar', 'invited', 'inviter',)
    search_fields = ('calendar', 'invited', 'inviter',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('calendar', 'invited', 'inviter', 'token',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('calendar', 'invited', 'inviter',)}
        ),
    )

admin.site.register(Invitation, InvitationAdmin)
