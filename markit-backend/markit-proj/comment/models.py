from django.db import models
from posts.models import Post
from collaboration.models import Collaborator

class Comment(models.Model):
    """
    Comment model.
    """
    collaborator = models.ForeignKey(Collaborator,
                                     related_name='comment_collaborator',
                                     on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.ForeignKey('self', related_name='reply_to',
                              on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.collaborator.user.email + ' posted a comment on ' + self.post.subject