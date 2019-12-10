from rest_framework import permissions
from collaboration.models import Collaborator

# obj is a Post instance

class OwnPermission(permissions.BasePermission):
    """
    Object level permission check for owner user.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is the owner of calendar or not.
        print("Check owner permission")
        return request.user == obj.calendar.owner

    def __str__(self):
        return 'Owner'



class ManagePermission(permissions.BasePermission):
    """
    Object level permission check for manager collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the managers of the calendar.
        print("Check manager permission")
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
            return collab.role == str(self)
        except:
            return False

    def __str__(self):
        return 'Manager'


class EditPermission(permissions.BasePermission):
    """
    Object level permission check for editor collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the editors of the calendar.
        print("Check editor permission")
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
            return collab.role == str(self)
        except:
            return False

    def __str__(self):
        return 'Editor'


class ViewPermission(permissions.BasePermission):
    """
    Object level permission check for viewer collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the viewers of the calendar.
        print("Check viewer permission")
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
            return collab.role == str(self)
        except:
            return False

    def __str__(self):
        return 'Viewer'
