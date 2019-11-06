from django import forms
from django.contrib import admin
from users.models import User
from .models import Calendar

class CalendarForm(forms.ModelForm):
    """
    Admin page calendar form.
    """
    name = forms.CharField(label="Name")
    collaborators = forms.ModelMultipleChoiceField(label='Collaborators', queryset=User.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Calendar
        fields = ('name', 'owner', 'collaborators')

class CalendarAdmin(admin.ModelAdmin):
    """
    Custom calendar admin page.
    """
    change_form = CalendarForm
    add_form = CalendarForm
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    ordering = ('id', 'name',)
    list_filter = ('id', 'name')
    search_fields = ('owner', 'name')
    filter_horizontal = ('collaborators',)

    fieldsets = (
        (None, {'fields': ('name', 'owner',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'collaborators',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
