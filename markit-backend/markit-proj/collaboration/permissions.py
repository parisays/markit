from rest_framework import permissions
from .consts import Access
from .models import Collaborator

class CollaboratorPermission(permissions.BasePermission):
    """
    Check collaborator access.
    """
    SAFE_ACCESS = {
        'post' : Access.ADD_COLLABORATOR,
                }

    # obj is Calendar instane.
    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS.get(request.method, []):
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False
