from haystack.views import SearchView
from .models import *
 
class MySeachView(SearchView):
    def extra_context(self):       #重载extra_context来添加额外的context内容
        context = super(MySeachView,self).extra_context()
        side_list = Moviebang.objects.filter(n_start='4')
        context['side_list'] = side_list
        return context