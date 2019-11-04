from django import forms
from django.contrib import admin
from calendars.models import Calendar
from .models import Post

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

admin.site.register(Post, PostAdmin)
