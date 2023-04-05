from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    """ Permission for Delete API """

    def has_permission(self, request, view): 
        return True
   
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE': 
            if request.user.is_superuser:   
                return True
            else:
                return False
        elif request.method in ['GET','PUT','PATCH']:
                return True
        else:
            return False
