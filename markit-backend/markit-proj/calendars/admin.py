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
    # collaborators = forms.ModelMultipleChoiceField(label='Collaborators',
    #                                           queryset=User.objects.all(),
    #                                           widget=forms.CheckboxSelectMultiple)

    # managers = forms.ModelMultipleChoiceField(label='Managers',
    #                                           queryset=User.objects.all(),
    #                                           widget=forms.CheckboxSelectMultiple)

    # editors = forms.ModelMultipleChoiceField(label='Editors',
    #                                          queryset=User.objects.all(),
    #                                          widget=forms.CheckboxSelectMultiple)

    # viewers = forms.ModelMultipleChoiceField(label='Viewers',
    #                                          queryset=User.objects.all(),
    #                                          widget=forms.CheckboxSelectMultiple)
    connectedPlatforms = forms.ChoiceField(label='Connected Platforms', widget=forms.Select)


    class Meta:
        model = Calendar
        # fields = ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms')
        fields = ('name', 'owner', 'connectedPlatforms')

class CalendarAdmin(admin.ModelAdmin):
    """
    Custom calendar admin page.
    """
    change_form = CalendarForm
    add_form = CalendarForm
    list_display = ('id', 'name', 'owner', 'connectedPlatforms')
    list_display_links = ('name',)
    ordering = ('id', 'owner', 'name', 'connectedPlatforms')
    list_filter = ('id', 'name', 'owner', 'connectedPlatforms')
    search_fields = ('owner', 'name')
    # filter_horizontal = ('managers', 'editors', 'viewers',)
    # filter_horizontal = ('collaborators',)

    fieldsets = (
        # (None, {'fields': ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms',)}),
        (None, {'fields': ('name', 'owner', 'connectedPlatforms',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # 'fields': ('name', 'owner', 'managers', 'editors', 'viewers', 'connectedPlatforms',)}
            'fields': ('name', 'owner', 'connectedPlatforms',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
