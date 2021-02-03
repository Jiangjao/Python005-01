from django.shortcuts import render
from .serializers import OrderSerializer
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework.parsers import JSONParser
from .models import Order
from .serializers import OrderSerializer, CreateUserSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import IsBuyerOrReadOnly
import pymysql
# Create your views here.


@api_view(['GET'])
# pk is id
def order_cancelling(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Http404

    conn = pymysql.connect('localhost', 'root', 'Dj224768', 'myshop')
    cursor = conn.cursor()
    sql_update = f'UPDATE checkstand_order SET cancel_flag="0" WHERE id="{id}";'
    
    try:
        cursor.execute(sql_update)
        conn.commit()
    except Exception as e:
        print(e)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    finally:
        cursor.close()
        conn.close()

@api_view(['GET','POST'])
def order_create(request):
    if request.method == 'GET':
        return Response(None, status=status.HTTP_200_OK)
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(buyer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GenericViewSet
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsBuyerOrReadOnly]
    
    # perform_create是必须得有，否则报错
    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class CreateOrderViewSet(viewsets.ModelViewSet):
    """
    创建用户订单路径
    """
    serializer_class = OrderSerializer
    queryset = ""
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsBuyerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)


class CreateUserViewSet(viewsets.ModelViewSet):
    """
    创建用户API路径
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        # 用户是否有效
        serializer.is_valid(raise_exception=True)
        # 有效就保存
        serializer.save()

        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    允许用户查看和编辑API路径（API endpoint）
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        serializer = self.get_serializer(user)
        data = serializer.data

        # 接收通知
        user_notify = User.objects.get(pk=user.pk)
        # notify_dict = model_to_dict(user_notify.notifications.unread().first(), fields=["verb",])
        
        new_dict= {}
        for obj in user_notify.notifications.unread():
            notify_dict = model_to_dict(obj, fields=["verb",])
            new_dict.setdefault("verb", []).append(notify_dict["verb"])
            # dict(data, **notify_dict)
        
        return Response(dict(data, **new_dict))

    











