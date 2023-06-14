from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
)

# env\Lib\site-packages\rest_framework\permissions.py 
# class IsAuthenticated(BasePermission)

class IsStaffOrReadOnly(BasePermission):
    # VSCode'da def has yazildiginda has_permission yapisi otomatik tamamlanir. Bu durum tum override'lar icin gecerlidir.
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # elif (request.user and request.user.is_staff):
        #     return True
        # else:
        #     return False

        # yukaridaki mantigin kisa hali:
        return (request.method in SAFE_METHODS or request.user.is_staff) 
    
class IsStaffOrOnlySelfObjects(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_staff
            or request.user.id == obj.user.id
        )
        # "detail": "You do not have permission to perform this action."