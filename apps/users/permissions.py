import imp
from rest_framework import permissions

# class IsOwnerOrReadOnly(permissions.BasePermission):
    
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.username == request.user


# # class IsCreator(permissions.BasePermission):
# #     def has_object_permission(self, request, view, obj):
# #         auth_user_id = request.user
# #         return obj.username == auth_user_id


class IsOwner(permissions.BasePermission):
    
    def has_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHOD:
            return True


        return obj.username == request.user



# class IsSuperUser(BasePermission):

#     def has_permission(self, request, view):
#         return request.user and request.user.is_superuser

# class IsOwner(BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.user:
#             if request.user.is_superuser:
#                 return True
#             else:
#                 return obj.username == request.user
#         else:
#             return False