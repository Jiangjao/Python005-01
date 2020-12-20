from django.shortcuts import render
from .models import Moviebang
# Create your views here.


def show_all_comments(request):
    movies = Moviebang.objects.all()
    for index in movies:
        print(index.name)
    # print(movies)
    # html = "<html><body>It is now %s.</body></html>" % movies[0].name,movies[0].hp_max,movies[0].hp_growth
    return render(request,'crabdouban/index.html',{'movies': movies})


# def search(request):
#     q = request.GET.get('q') # 接收搜索关键字
#     error_msg = '' # 搜索错误返回提升内容
#     if not q: # 无搜索关键字时处理方法
#         error_msg = '请输入关键词'
#         return render(request, 'django_app_www/error.html', {'error_msg': error_msg})
#     post_list = Share_info.objects.filter(name__icontains=q) # 开始搜索
#     paginator = Paginator(post_list,27,5)# 对搜索结果分页处理，每页27条，不足5条的结果合并到上一页
#     page = request.GET.get('page') # 看看请求中是否带有页码 ，这个貌似没用，主要省事使用默认页面的代码
#     try:
#         customer = paginator.page(page)
#     except PageNotAnInteger:
#         customer = paginator.page(1)
#     except EmptyPage:
#         customer = paginator.page(paginator.num_pages)

#     return render(request,'django_app_www/test.html',{ 'cus_list' : customer })# 渲染页面