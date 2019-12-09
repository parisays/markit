from rest_framework import permissions
from collaboration.models import Collaborator

ADD_COLLABORATOR = 'A'
DELETE_CALENDAR = 'B'
UPDATE_CALENDAR = 'C'
VIEW_CALENDAR = 'D'
CREATE_POST = 'E'
UPDATE_POST = 'F'
VIEW_POST = 'G'
DELETE_POST = 'H'
POST_COMMENT = 'I'
SET_PUBLISH = 'J'


# obj is a Calendar instance

class OwnPermission(permissions.BasePermission):
    """
    Object level permission check for owner user.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is the owner of calendar or not.
        print("Check owner permission")
        return request.user == obj.owner

    def __str__(self):
        return 'Owner'

    @classmethod
    def get_access(cls):
        """
        Return list of Owner's access.
        """
        return [ADD_COLLABORATOR, DELETE_CALENDAR, UPDATE_CALENDAR, VIEW_CALENDAR,
                CREATE_POST, UPDATE_POST, VIEW_POST, DELETE_POST, POST_COMMENT, SET_PUBLISH]


class ManagePermission(permissions.BasePermission):
    """
    Object level permission check for viewr collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the managers of the calendar.
        print("Check manager permission")
        collab = Collaborator.objects.filter(user=request.user).filter(calendar=obj)
        return len(collab) >=1

    def __str__(self):
        return 'Manager'

    @classmethod
    def get_access(cls):
        """
        Return list of Manager's access.
        """
        return [VIEW_CALENDAR, CREATE_POST, UPDATE_POST, VIEW_POST,
                DELETE_POST, POST_COMMENT, SET_PUBLISH]


class EditPermission(permissions.BasePermission):
    """
    Object level permission check for editor collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the editors of the calendar.
        print("Check editor permission")
        collab = Collaborator.objects.filter(user=request.user).filter(calendar=obj)
        return len(collab) >=1

    def __str__(self):
        return 'Editor'

    @classmethod
    def get_access(cls):
        """
        Return list of Owner's access.
        """
        return [ADD_COLLABORATOR, DELETE_CALENDAR, UPDATE_CALENDAR,
                VIEW_CALENDAR, CREATE_POST, UPDATE_POST, VIEW_POST, DELETE_POST, POST_COMMENT]


class ViewPermission(permissions.BasePermission):
    """
    Object level permission check for viewr collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Checks if user is one of the viewers of the calendar.
        print("Check viewer permission")
        collab = Collaborator.objects.filter(user=request.user).filter(calendar=obj)
        return len(collab) >=1

    def __str__(self):
        return 'Viewer'

    @classmethod
    def get_access(cls):
        """
        Return list of Owner's access.
        """
        return [VIEW_CALENDAR, VIEW_POST, POST_COMMENT]
