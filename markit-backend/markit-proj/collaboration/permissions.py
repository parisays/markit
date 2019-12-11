from rest_framework import permissions
# from .models import Collaborator
from .consts import Access

class InviteCollaboratorPermission(permissions.BasePermission):
    """
    Check invite collaborator access.
    """
    SAFE_ACCESS = [Access.ADD_COLLABORATOR]

    # obj is Calendar instane.
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
        # try:
        #     collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
        #     for access in self.SAFE_ACCESS:
        #         if access not in collab.role.access:
        #             return False
        #     return True
        # except:
        #     return False
