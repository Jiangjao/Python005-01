from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Order

# HyperlinkedModelSerializer 的作用类似url

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    订单序列
    """
    buyer = serializers.ReadOnlyField(source='buyer.username')
    
    # 指明数据库和可显示字段
    # 注意id是Djang自动创建的
    class Meta:
        model = Order
        fields = ['id', 'product_id', 'buyer', 'cancel_flag', 'createtime']


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    创建用户序列
    """
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', ]
    
    def validate(self, attrs):
        # 对密码进行加密
        attrs['password'] = make_password(attrs['password'])
        return attrs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    展示用户-订单序列
    """
    orders = OrderSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'orders', ]