from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from rest_framework.permissions import IsAuthenticated


class UserCreationForm(forms.ModelForm):
    firstName = forms.CharField(label='First Name')
    lastName = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def check_password_confirmation(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label= ("Password"),
     help_text= ("Raw passwords are not stored, so there is no way to see "))
                        
    class Meta:
        model = User
        fields = ('email', 'password', 'is_staff', 'profileImage')

    def clean_password(self):
        return self.initial["password"]



class CustomUserAdmin(UserAdmin):
    change_form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id', 'email', 'firstName', 'lastName')
    UserAdmin.list_display_links = ('email',)
    ordering = ('id', 'email', 'firstName', 'lastName')
    list_filter = ('email',)
    search_fields = ('email',)
    filter_horizontal = ()
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstName', 'lastName', 'profileImage')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstName', 'lastName', 'password1', 'password2', 'is_staff')}
        ),
    )

admin.site.register(User, CustomUserAdmin)



