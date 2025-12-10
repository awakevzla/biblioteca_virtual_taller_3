from rest_framework import permissions

class IsAdminOrSuperuser(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso solo a administradores y superusuarios.
    """
    def has_permission(self, request, view):
        # Verificar que el usuario esté autenticado
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Permitir acceso si es superusuario o tiene rol de admin
        return request.user.is_superuser or request.user.rol == 'admin'
