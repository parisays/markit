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
    managers = forms.ModelMultipleChoiceField(label='Managers',
                                              queryset=User.objects.all(),
                                              widget=forms.CheckboxSelectMultiple)

    editors = forms.ModelMultipleChoiceField(label='Editors',
                                             queryset=User.objects.all(),
                                             widget=forms.CheckboxSelectMultiple)

    viewers = forms.ModelMultipleChoiceField(label='Viewers',
                                             queryset=User.objects.all(),
                                             widget=forms.CheckboxSelectMultiple)
    connectedPlatforms = forms.ChoiceField(label='Connected Platforms', widget=forms.Select)


    class Meta:
        model = Calendar
        fields = ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms')

class CalendarAdmin(admin.ModelAdmin):
    """
    Custom calendar admin page.
    """
    change_form = CalendarForm
    add_form = CalendarForm
    list_display = ('id', 'name', 'owner', 'connectedPlatforms')
    list_display_links = ('id', 'owner', 'connectedPlatforms')
    ordering = ('id', 'owner', 'name', 'managers', 'editors', 'viewers', 'connectedPlatforms')
    list_filter = ('id', 'name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms')
    search_fields = ('owner', 'name')
    filter_horizontal = ('managers', 'editors', 'viewers',)

    fieldsets = (
        (None, {'fields': ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
