from .models import Role

class Access():
    """
    All accesses.
    """
    ADD_COLLABORATOR = 'add_collaborator'
    DELETE_CALENDAR = 'delete_calendar'
    EDIT_CALENDAR = 'edit_calendar'
    VIEW_CALENDAR = 'view_calendar'
    CREATE_POST = 'create_post'
    EDIT_POST = 'edit_post'
    VIEW_POST = 'view_post'
    DELETE_POST = 'delete_post'
    POST_COMMENT = 'post_comment'
    SET_PUBLISH = 'set_publish'
    SET_PUBLISH_WITH_PERMISSION = 'set_publish_with_permission'

class DefinedRoles():
    """
    All roles.
    """
    OWNER = 'Owner'
    MANAGER = 'Manager'
    EDITOR = 'Editor'
    VIEWER = 'Viewer'

    DEFAULT_ROLES = {OWNER : [Access.ADD_COLLABORATOR, Access.DELETE_CALENDAR,
                              Access.  EDIT_CALENDAR, Access.VIEW_CALENDAR,
                              Access.CREATE_POST, Access.EDIT_POST,
                              Access.VIEW_POST, Access.DELETE_POST,
                              Access.POST_COMMENT, Access.SET_PUBLISH],
                     MANAGER : [Access.VIEW_CALENDAR, Access.CREATE_POST,
                                Access.EDIT_POST, Access.VIEW_POST,
                                Access.DELETE_POST, Access.POST_COMMENT,
                                Access.SET_PUBLISH],
                     EDITOR : [Access.VIEW_CALENDAR, Access.CREATE_POST,
                               Access.EDIT_POST, Access.VIEW_POST,
                               Access.DELETE_POST, Access.POST_COMMENT,
                               Access.SET_PUBLISH_WITH_PERMISSION],
                     VIEWER : [Access.VIEW_CALENDAR, Access.VIEW_POST,
                               Access.POST_COMMENT]
                    }

    @staticmethod
    def set_role_access(role_name, access):
        """
        Set access for each role.
        """
        return DefinedRoles.DEFAULT_ROLES.get(role_name, access)

    # @staticmethod
    # def create_default_roles():
    #     """
    #     Create default roles for the for the first time.
    #     """
    #     for role in DefinedRoles.DEFAULT_ROLES:
    #         current_role = Role.objects.create(name=role,
    #                         access=DefinedRoles.set_role_access(role_name=role, access=[]))
    #         cu
    

