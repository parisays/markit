from django.db import models
from posts.models import Post
from users.models import User

class Comment(models.Model):
    """
    Comment model.
    """
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.ForeignKey('self', related_name='reply_to',
                              on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return self.user.id + '|' + self.post.subject