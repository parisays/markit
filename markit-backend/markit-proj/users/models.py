from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from stdimage.models import StdImageField

class UserManager(BaseUserManager):
    """
    User manager.
    """
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password=None,
                    profile_image=None, is_staff=False):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            profile_image=profile_image,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    User model.
    """
    email = models.EmailField('Email Address', unique=True, max_length = 255)
    username = None
    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('Last Name', max_length=50)

    profileImage = StdImageField(verbose_name='Profile Picture', editable=True,
                                 blank=True, upload_to='profileImage',
                                 default='static/profile.jpg',
                                 variations={'thumbnail' :
                                 {"width":100, "height":100, "crop":True}})

    is_staff = models.BooleanField('Staff', default=False,
                                   help_text=('Designates whether the user can log into this admin '
                                              'site.'))
    is_admin = models.BooleanField('Admin', default=False)
    is_active = models.BooleanField('Active', default=True,
                                    help_text=('Designates whether this user should be treated as '
                                               'active. Use this instead of deleting accounts.'))

    def __unicode__(self):
        return "{0}".format(self.profileImage)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return self.email

    objects = UserManager()
