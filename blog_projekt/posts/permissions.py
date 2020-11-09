from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """overrides permission's base class"""

    def has_object_permission(self, request, view, obj):
        # read only permissions are allowed for any request but write 
        # permissions only reserved for author of post
        if request.method in permissions.SAFE_METHODS:
            # SAFE_METHODS are GET, OPTIONS, HEAD
            return True

        return obj.author == request.user
        



