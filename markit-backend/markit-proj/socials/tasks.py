import os
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from rest_framework.renderers import JSONRenderer
from celery import shared_task
import tweepy
import json
from posts.models import Post
from calendars.models import Calendar
from socials.models import SocialAccount


def create_tweet_task(post_id):
    """
    Create a django celery beat PeriodicTask with ClockedSchedule for each post.
    """
    post = Post.objects.get(pk=post_id)
    clocked_schedule = ClockedSchedule(clocked_time=post.publishDateTime)
    clocked_schedule.save()

    task_data = dict(
        name="PublishTweet{}".format(str(post_id)),
        task="socials.tasks.publish_tweet_job",
        clocked=clocked_schedule,
        kwargs=json.dumps({"post_id":str(post_id)})
    )
    periodic_task = PeriodicTask(**task_data)
    periodic_task.enabled = True
    periodic_task.one_off = True
    periodic_task.save()
    post.publishTask = periodic_task
    post.save()


@shared_task
def publish_tweet_job(post_id):
    """
    Publish tweets in their time.
    Runs immediately in the publish time of the post.
    """
    post = Post.objects.get(pk=post_id)
    if post.status == 'Published':
        return "Tweet has been published previously."
    calendar = Calendar.objects.get(pk=post.calendar.id)
    twitter_account = SocialAccount.objects.get(calendar=calendar)
    access_token = twitter_account.token
    secret_token = twitter_account.tokenSecret
    twitter_app = twitter_account.app
    auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret)
    auth.set_access_token(access_token, secret_token)
    twitter_api = tweepy.API(auth)
    image_path = post.image.path
    if os.path.exists(image_path):
        twitter_api.update_with_media(image_path, status=post.text)
    else:
        twitter_api.update_status(post.text)
    post.status = 'Published'
    post.save()
    return "Tweet sent successfully."

