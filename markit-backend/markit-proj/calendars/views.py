from itertools import chain
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from collaboration.models import Collaborator
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from calendars.serializers import (
    NestedCalendarSerializer,
    CalendarSerializer,
)
from users.models import User
from .permissions import (
    OwnPermission,
    ManagePermission,
    EditPermission,
    ViewPermission,
)
from collaboration.views import CollaboratorCreateView

class CalendarListCreateView(generics.ListCreateAPIView):
    """
    Create and list calendars view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Calendar.objects.all()
    serializer_class = NestedCalendarSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        request.data.update({'owner' : user.id})
        request.data.update({'posts' : []})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        collab_view = CollaboratorCreateView.as_view()
        collab_view(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        calendar_list = Calendar.objects.filter(owner=user)
        # Add calendars that user is a manager/editor/viewer of.

        # manage_list = Calendar.objects.filter(managers=user)
        # edit_list = Calendar.objects.filter(editors=user)
        # view_list = Calendar.objects.filter(viewers=user)
        # collab = Collaborator.objects.filter(user=user)
        # collab_list = Calendar.objects.filter(collaborators=collab)
        # calendar_list = list(chain(own_list, manage_list, edit_list, view_list))
        # calendar_list = list(chain(own_list, collab_list))
        serializer = self.get_serializer(calendar_list, many=True)
        return Response(serializer.data)

class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Destroy calendar view.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()

    def update(self, request, *args, **kwargs):
        # self.permission_classes = (IsAuthenticated, OwnPermission)
        self.serializer_class = CalendarSerializer
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # self.permission_classes = (IsAuthenticated, OwnPermission)
        self.serializer_class = NestedCalendarSerializer
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        # self.permission_classes = (IsAuthenticated, OwnPermission,
        #                            ManagePermission, EditPermission, ViewPermission)
        self.serializer_class = NestedCalendarSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Append role access
        # access = perm.get_access()
        # data = {'access' : access}
        # data.update(serializer.data)
        return Response(serializer.data)

    # def check_object_permissions(self, request, obj):
    #     """
    #     Check if the request should be permitted for a given object.
    #     Raises an appropriate exception if the request is not permitted.
    #     """
    #     perms = []
    #     for permission in self.get_permissions():
    #         if permission.has_object_permission(request, self, obj):
    #             # perms.append(permission.__str__())
    #             perms.append(permission)
    #     if len(perms) <= 1:
    #         self.permission_denied(request)
    #     return perms[1]

    # def get_object(self):
    #     """
    #     Returns the object the view is displaying.

    #     You may want to override this if you need to provide non-standard
    #     queryset lookups.  Eg if objects are referenced using multiple
    #     keyword arguments in the url conf.
    #     """
    #     queryset = self.filter_queryset(self.get_queryset())

    #     # Perform the lookup filtering.
    #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

    #     assert lookup_url_kwarg in self.kwargs, (
    #         'Expected view %s to be called with a URL keyword argument '
    #         'named "%s". Fix your URL conf, or set the `.lookup_field` '
    #         'attribute on the view correctly.' %
    #         (self.__class__.__name__, lookup_url_kwarg)
    #     )

    #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    #     obj = get_object_or_404(queryset, **filter_kwargs)

    #     # May raise a permission denied
    #     perm = self.check_object_permissions(self.request, obj)

    #     return (obj, perm)
