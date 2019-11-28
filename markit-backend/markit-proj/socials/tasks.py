# import os
from django_celery_beat.models import PeriodicTask, ClockedSchedule
# from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer
from celery import shared_task
import tweepy
# import requests
from posts.models import Post
# from posts.serializers import PostSerializer
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
        name="PublishTweet",
        task="socials.tasks.publish_tweet_job",
        clocked=clocked_schedule,
        kwargs=JSONRenderer().render(data={"post_id":str(post_id)})
    )
    periodic_task = PeriodicTask(**task_data)
    periodic_task.enabled = True
    periodic_task.one_off = True
    periodic_task.save()


@shared_task
def publish_tweet_job(post_id):
    """
    Publish tweets in their time.
    Runs immediately in the publish time of the post.
    """
    post = Post.objects.get(pk=post_id)
    if post.status == 'Published':
        return "Tweet has already been published."
    calendar = Calendar.objects.get(pk=post.calendar.id)
    twitter_account = SocialAccount.objects.get(calendar=calendar)
    access_token = twitter_account.token
    secret_token = twitter_account.tokenSecret
    twitter_app = twitter_account.app
    auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret)
    auth.set_access_token(access_token, secret_token)
    twitter_api = tweepy.API(auth)
    # image_url = Request.build_absolute_uri(PostSerializer(post).data['image'])
    # image_file = 'temp.jpg'
    # request = requests.get(image_url, stream=True)
    # if request.status_code == 200:
    #     with open(image_file, 'wb') as image:
    #         for chunk in request:
    #             image.write(chunk)
    #     twitter_api.update_with_media(image_file, status=post.text)
    #     os.remove(image_file)
    # else:
    #     twitter_api.update_status(post.text)
    twitter_api.update_status(post.text)
    post.status = 'Published'
    post.save()
    return "Tweet sent successfully."

