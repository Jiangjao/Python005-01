from rest_framework import permissions

class IsBuyerOrReadOnly(permissions.BasePermission):
    """
    只有该用户才能编辑它
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 总是允许GET, HEAD或OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 订单的创建者才能编辑
        return obj.buyer == request.user







