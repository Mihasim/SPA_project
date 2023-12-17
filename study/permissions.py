from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    """
    доступ для владельца
    """
    manage = "Вы не являетесь владельцем"
    def has_permission(self, request, view):
        return request.user == view.get_object().owner


class IsModerator(BasePermission):
    """
    доступ для модератора
    """
    manage = "Вы не являетесь модератором"
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                group = request.user.groups.all()[0].name
                if group == 'Модератор':
                    return True
            except IndexError:
                return False


class IsOwnerOrStaff(BasePermission):
    """
    доступ для модератора или владельца
    """
    manage = "Вы не являетесь владельцем или модератором"
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                group = request.user.groups.all()[0].name
                if group == 'Модератор':
                    return True
            except IndexError:
                return False

            return request.user == view.get_object().owner


class CoursePermission(BasePermission):
    """
    доступ для модератора или владельца курса для DRF
    """
    def has_permission(self, request, view):
        print()
        if request.method == 'POST':
            return IsAuthenticated()
        elif request.method in ['GET', 'PATCH', 'PUT']:
            return IsAuthenticated() and (IsOwner() or IsModerator())
        elif request.method == 'DELETE':
            return IsOwner()
        return False
