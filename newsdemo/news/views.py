from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewsIdSerializer
from .models import DemoNewsModel
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

@api_view(['GET', 'POST'])
def get_data_from_API(request):
    news_list = DemoNewsModel.objects.all()
    if request.method == 'POST':
        DemoNewsModel.objects.create(**request.data)
        return Response({"Record inserted successfully.": request.data})
    serialized = NewsIdSerializer(news_list, many=True)
    return Response(serialized.data)


def newsItemView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print("q is: ", q)
    news_list = DemoNewsModel.objects.filter(Q(name__icontains=q))
    print("News query is: ", news_list.query)
    print("Query set: ", news_list)
    p = Paginator(DemoNewsModel.objects.filter(Q(name__icontains=q)), 5)
    page = request.GET.get('page')
    news = p.get_page(page)
    nums = "1" * news.paginator.num_pages
    return render(request, 'news/news.html', {'news': news, 'news_list':  news_list, "nums": nums})