from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    product_id = models.CharField(max_length=50)
    buyer = models.ForeignKey(
        'auth.User', related_name='orders', on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)
    cancel_flag = models.CharField(max_length=5, default='0')

    class Meta:
        ordering = ['createtime']
    
    def __str__(self):
        return self.product_id
