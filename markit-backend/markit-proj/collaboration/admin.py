from django import forms
from django.contrib import admin
from .models import Collaborator, Role
from users.models import User
from calendars.models import Calendar

class RoleForm(forms.ModelForm):
    """
    Admin page role form.
    """
    name = forms.CharField(label='Name')
    access = forms.CharField(label='Access', widget=forms.Textarea)

    class Meta:
        model = Role
        fields = ('name', 'access',)

class RoleAdmin(admin.ModelAdmin):
    """
    Custom role admin page.
    """
    change_form = RoleForm
    add_form = RoleForm
    list_display = ('id', 'name', 'access',)
    list_display_links = ('name',)
    ordering = ('id', 'name', 'access',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('name', 'access',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'access',)}
        ),
    )

class ColaboratorForm(forms.ModelForm):
    """
    Admin page collaborator form.
    """
    user = forms.ModelChoiceField(label='User', queryset=User.objects.all(),
                                      widget=forms.CheckboxSelectMultiple)
    calendar = forms.ModelChoiceField(label='Calendar', queryset=Calendar.objects.all(),
                                      widget=forms.CheckboxSelectMultiple)

    role = forms.ModelChoiceField(label='Role', queryset=Role.objects.all(),
                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Collaborator
        fields = ('user', 'calendar', 'role',)


class CollaboratorAdmin(admin.ModelAdmin):
    """
    Custom collaborator admin page.
    """
    change_form = ColaboratorForm
    add_form = ColaboratorForm
    list_display = ('id', 'calendar', 'user', 'role',)
    ordering = ('id', 'user', 'calendar', 'role',)
    list_filter = ('user', 'calendar', 'role',)
    search_fields = ('calendar', 'user', 'role',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('calendar', 'user', 'role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('calendar', 'user', 'role',)}
        ),
    )

admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Role, RoleAdmin)