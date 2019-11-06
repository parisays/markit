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
    connected_platforms = forms.ChoiceField(label='Connected Platforms', widget=forms.Select)


    class Meta:
        model = Calendar
        fields = ('name', 'owner', 'collaborators', 'connected_platforms')

class CalendarAdmin(admin.ModelAdmin):
    """
    Custom calendar admin page.
    """
    change_form = CalendarForm
    add_form = CalendarForm
    list_display = ('id', 'name', 'owner','connected_platforms')
    list_display_links = ('id', 'owner', 'connected_platforms')
    ordering = ('id', 'owner', 'name', 'collaborators', 'connected_platforms')
    list_filter = ('id', 'name', 'owner', 'collaborators', 'connected_platforms')
    search_fields = ('owner', 'name')
    filter_horizontal = ('collaborators',)

    fieldsets = (
        (None, {'fields': ('name', 'owner', 'collaborators', 'connected_platforms',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'owner', 'collaborators', 'connected_platforms',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
