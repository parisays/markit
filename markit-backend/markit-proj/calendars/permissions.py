from rest_framework import permissions

class ViewPermission(permissions.BasePermission):
    """
    Object level permission check for viewr collaborators.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user

class EditPermission(permissions.BasePermission):
    """
    Object level permission check for editor collaborators.
    """

class ManagePermission(permissions.BasePermission):
    """
    Object level permission check for viewr collaborators.
    """
