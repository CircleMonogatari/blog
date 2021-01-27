from django.core.paginator import PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.views import View
from pure_pagination import Paginator

from blog_admin import models


class IndexView(View):
    """
    博客首页
    """

    def get(self, request):
        all_blog = models.Blog.objects.all().order_by('-id')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 5, request=request)  # 每页显示5条
        all_blog = p.page(page)

        return render(request, 'blog_admin\index.html', context={'all_blog': all_blog})
