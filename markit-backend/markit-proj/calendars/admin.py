from django import forms
from django.contrib import admin
from users.models import User
from .models import Calendar

class CalendarForm(forms.ModelForm):
    """
    Admin page calendar form.
    """
    name = forms.CharField(label="Name")
    owner = forms.ModelChoiceField(label='Owner', queryset=User.objects.all(), empty_label=None)
    collaborators = forms.ModelMultipleChoiceField(label='Collaborators',
                                                   queryset=User.objects.all(),
                                                   widget=forms.CheckboxSelectMultiple)
    connectedPlatforms = forms.ChoiceField(label='Connected Platforms', widget=forms.Select)


    class Meta:
        model = Calendar
        fields = ('name', 'owner', 'collaborators', 'connectedPlatforms')

class CalendarAdmin(admin.ModelAdmin):
    """
    Custom calendar admin page.
    """
    change_form = CalendarForm
    add_form = CalendarForm
    list_display = ('id', 'name', 'owner','connectedPlatforms')
    list_display_links = ('id', 'owner', 'connectedPlatforms')
    ordering = ('id', 'owner', 'name', 'collaborators', 'connectedPlatforms')
    list_filter = ('id', 'name', 'owner', 'collaborators', 'connectedPlatforms')
    search_fields = ('owner', 'name')
    filter_horizontal = ('collaborators',)

    fieldsets = (
        (None, {'fields': ('name', 'owner', 'collaborators', 'connectedPlatforms',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'owner', 'collaborators', 'connectedPlatforms',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
