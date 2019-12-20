from rest_framework import permissions
from collaboration.models import Collaborator
from collaboration.consts import Access

class PostPermission(permissions.BasePermission):
    """
    Check post access.
    """
    SAFE_ACCESS = {
        'get':Access.VIEW_POST,
        'put':Access.EDIT_POST,
        'patch':Access.EDIT_POST,
        'delete':Access.DELETE_POST,
    }

    # obj is a Post instance
    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
            for access in self.SAFE_ACCESS.get(request.method, []):
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False

class CreatePostPermission(permissions.BasePermission):
    """
    Check create post access.
    """
    SAFE_ACCESS = [Access.CREATE_POST]

    # obj is a Calendar instance
    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False

# class UpdatePostPermission(permissions.BasePermission):
#     """
#     Check update post access.
#     """
#     SAFE_ACCESS = [Access.EDIT_POST]

#     # obj is a Post instance
#     def has_object_permission(self, request, view, obj):
#         try:
#             collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
#             for access in self.SAFE_ACCESS:
#                 if access not in collab.role.access:
#                     return False
#             return True
#         except:
#             return False

# class DestroyPostPermission(permissions.BasePermission):
#     """
#     Check destroy post access.
#     """
#     SAFE_ACCESS = [Access.DELETE_POST]

#     # obj is a Post instance
#     def has_object_permission(self, request, view, obj):
#         try:
#             collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
#             for access in self.SAFE_ACCESS:
#                 if access not in collab.role.access:
#                     return False
#             return True
#         except:
#             return False

# class RetrievePostPermission(permissions.BasePermission):
#     """
#     Check retrieve post access.
#     """
#     SAFE_ACCESS = [Access.VIEW_POST]

#     # obj is a Post instance
#     def has_object_permission(self, request, view, obj):
#         try:
#             collab = Collaborator.objects.filter(user=request.user).get(calendar=obj.calendar)
#             for access in self.SAFE_ACCESS:
#                 if access not in collab.role.access:
#                     return False
#             return True
#         except:
#             return False