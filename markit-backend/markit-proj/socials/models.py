from django.db import models
from calendars.models import Calendar

TWITTER = 'Twitter'
PROVIDERS = [
    (TWITTER, 'Twitter'),
]

class SocialApp(models.Model):
    """
    Social App model.
    contains twitter developer app info.
    """
    provider = models.CharField(unique=True, verbose_name='provider',
                                max_length=30,
                                choices=PROVIDERS)
    name = models.CharField(verbose_name='name',
                            max_length=40)
    clientId = models.CharField(verbose_name='client id',
                                max_length=191,
                                help_text='App ID, or consumer key')
    secret = models.CharField(verbose_name='secret key',
                              max_length=191,
                              help_text='API secret, client secret, or'
                              ' consumer secret')
    class Meta:
        verbose_name = 'social application'
        verbose_name_plural = 'social applications'

    def __str__(self):
        return self.name


class SocialAccount(models.Model):
    """
    Social Account model.
    contains info and credentials of the social account.
    """
    app = models.ForeignKey(SocialApp, related_name='socialaccount_app', on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, related_name='socialaccount_calendar',
                                 on_delete=models.CASCADE)
    provider = models.CharField(verbose_name='provider',
                                max_length=30,
                                choices=PROVIDERS)
    token = models.TextField(
        verbose_name='token',
        help_text='"oauth_token" (OAuth1) or access token (OAuth2)')
    tokenSecret = models.TextField(
        blank=True,
        verbose_name='token secret',
        help_text='"oauth_token_secret" (OAuth1) or refresh token (OAuth2)')
    expireDate = models.DateTimeField(blank=True, null=True,
                                      verbose_name='expires at')


    class Meta:
        verbose_name = 'social account'
        verbose_name_plural = 'social accounts'
