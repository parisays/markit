from django import forms
from django.contrib import admin
from .models import *



class CalendarForm(forms.ModelForm):
    """
    Admin page calendar form.
    """
    name = forms.CharField(label="Name")
    user = forms.ModelMultipleChoiceField(label='Users', queryset=User.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Calendar
        fields = ('name', 'user')

class PostForm(forms.ModelForm):
    """
    Admin page post form.
    """
    name = forms.CharField(label='Name')
    text = forms.CharField(label='Text', widget=forms.Textarea)
    calendar = forms.ModelChoiceField(label='Calendar', queryset=Calendar.objects.all(),
                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ('name', 'text', 'calendar')

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
    search_fields = ('user', 'name')
    filter_horizontal = ('user',)

    fieldsets = (
        (None, {'fields': ('name', 'user',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'user',)}
        ),
    )

class PostAdmin(admin.ModelAdmin):
    """
    Custom post admin page.
    """
    change_form = PostForm
    add_form = PostForm
    list_display = ('id', 'name', 'calendar')
    list_display_links = ('id',)
    ordering = ('id', 'name', 'calendar',)
    list_filter = ('calendar',)
    search_fields = ('calendar', 'name')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('name', 'calendar', 'text',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'calendar', 'text',)}
        ),
    )


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Post, PostAdmin)
