from django.urls import path,register_converter,re_path

from . import views
from haystack.views import SearchView

# 自定义过滤器
# register_converter(converters.IntConverter,'myint')
# register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.show_all_comments, name='index'),
    path('index', views.show_all_comments, name='index'),
    # path('search/', views.search,name='search'),
    path('search/', SearchView(), name='haystack_search'),
]