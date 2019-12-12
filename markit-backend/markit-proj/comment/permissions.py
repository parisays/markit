from rest_framework import permissions
from collaboration.models import Collaborator
from collaboration.consts import Access

class CommentPermission(permissions.BasePermission):
    """
    Check comment access.
    """
    SAFE_ACCESS = [Access.POST_COMMENT]
    # obj is a Post instance
    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False

class CommentViewPermission(permissions.BasePermission):
    """
    Check comment access.
    """
    SAFE_ACCESS = [Access.POST_COMMENT]
    # obj is a Comment instance
    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.post.calendar)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False