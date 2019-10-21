from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.firstName = data.get('firstName')
        user.lastName = data.get('lastName')
        user.set_password(data.get('password'))
        user.save()
        return user