from django.urls import path, include
from shoptest import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet, )
router.register(r'usersapi', views.CreateUserViewSet, 'user_api')
router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('orders/create/', views.order_create),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('orders/<int:id>/cancel/', views.order_cancelling),
    # path('viewset/<int:pk>/', include(router.urls)),
    # path('orders/', order_list),
    # path('orders/', OrderAPIView.as_view()),
    # path('orders/<int:pk>', order_detail),
    # path('orders/<int:id>/', OrderDetailView.as_view()),
    # path('orders/', OrderGenericAPIView.as_view()),
    # path('orders/<int:id>/', OrderGenericAPIView.as_view()),
]