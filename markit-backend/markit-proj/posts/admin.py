from django import forms
from django.contrib import admin
from calendars.models import Calendar
from .models import Post

class PostForm(forms.ModelForm):
    """
    Admin page post form.
    """
    subject = forms.CharField(label='Subject')
    text = forms.CharField(label='Text', widget=forms.Textarea)
    status = forms.ChoiceField(label='Status', widget=forms.Select)
    calendar = forms.ModelChoiceField(label='Calendar', queryset=Calendar.objects.all(),
                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ('subject', 'text', 'status', 'calendar')

class PostAdmin(admin.ModelAdmin):
    """
    Custom post admin page.
    """
    change_form = PostForm
    add_form = PostForm
    list_display = ('id', 'subject', 'status', 'calendar')
    list_display_links = ('id',)
    ordering = ('id', 'subject', 'status', 'calendar',)
    list_filter = ('status', 'calendar',)
    search_fields = ('calendar', 'subject')
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('subject', 'status', 'calendar', 'text',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('subject', 'status', 'calendar', 'text',)}
        ),
    )

admin.site.register(Post, PostAdmin)
