from django.contrib import admin
from calendars.models import *
from django import forms

admin.site.register(Calendar)
admin.site.register(Post)

class CalendarForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    user = forms.ModelMultipleChoiceField(label='user', queryset = User.objects.all())

    class Meta:
        model = Calendar
        fields = ('name', 'user')

class PostForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    text = forms.CharField(label='Text', widget=forms.Textarea)
    calendar = forms.ModelChoiceField(label='Calendar', queryset = Calendar.objects.all())

    class Meta:
        model = Post
        fields = ('name', 'text', 'calendar')