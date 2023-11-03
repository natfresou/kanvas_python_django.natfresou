from rest_framework import permissions
from rest_framework.views import View
from accounts.models import Account
from courses.models import Course
from contents.models import Content

class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return False

class IsSuperuserOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Account) -> bool:
        return request.user.is_superuser or obj == request.user

class IsSuperuserOrOwnerForGet(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Content) -> bool:
        if request.method in permissions.SAFE_METHODS and request.user in obj.course.students.all():
            return True
        if request.user.is_superuser:
            return True
        return False
    
class IsSuperuserOrOwnerForGet2(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Course) -> bool:
        if request.method in permissions.SAFE_METHODS and obj == request.user:
            print(obj,"obj")
            print(request.user,"request.user")
            return True
        if request.user.is_superuser:
            return True
        return False

class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):  
        return  request.user.is_superuser