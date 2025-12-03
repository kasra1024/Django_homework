from rest_framework.permissions import BasePermission


class IsStudent (BasePermission):

    def has_permission(self, request, view):
        return request.user.profile.is_student


class IsTeacher (BasePermission):
     
     def has_permission(self, request, view):
        return not request.user.profile.is_student
     
# ی دونه obj
class ActiveCourse(BasePermission) :
    message = "اجازه ندارد" 
    def has_object_permission(self, request, view, obj):
        return obj.active
