from django import forms
from django.contrib import admin
from users.models import User
from .models import Calendar

class CalendarForm(forms.ModelForm):
    """
    Admin page calendar form.
    """
    name = forms.CharField(label="Name")
    users = forms.ModelMultipleChoiceField(label='Users', queryset=User.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Calendar
        fields = ('name', 'users')

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
    search_fields = ('users', 'name')
    filter_horizontal = ('users',)

    fieldsets = (
        (None, {'fields': ('name', 'users',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'users',)}
        ),
    )

admin.site.register(Calendar, CalendarAdmin)
