from django.shortcuts import render
import json
import requests
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import NewsIdSerializer
from .models import DemoNewsModel
from django.core.paginator import Paginator

# Create your views here.


class NewsIdView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsIdSerializer


# get a list of all news ids from hacker news

    def get(self, request, format=None):

        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)

        result = response.text.split(',')[1:len(
            response.text.split(','))-2]  # to trim the last element
        # got this from API " 499287535 ] /n" --> reshaped to that below
        last = response.text.split(',')[-1]
        result.insert(len(result), last.strip().split()[0])  # "499287535"

        # list comprehension to strip each element of the data
        res = [int(id.strip()) for id in result]

        return Response(res, status=status.HTTP_200_OK)


class NewsItemView(APIView):
    permission_classes = [AllowAny]
    serializer_class = NewsIdSerializer

    def get_data_from_API(self):
        """
            This helps to return
            formatted data fetched from endpoint provided
            using request.
        """
        # latest = DemoNewsModel.objects.all()[len(DemoNewsModel.objects.all())-1].hackernews # getting latest id from db
        result = []
        # half = 0
        # getting the total ids from the db
        # total = len(DemoNewsModel.objects.all())

        # slicing into half based on even or odd total
        # if total % 2 == 0:
        #     half = len(DemoNewsModel.objects.all()) / 2
        # else:
        #     half = (len(DemoNewsModel.objects.all()) / 2) + 1

        # slicing the queryset to get last half
        # ids = DemoNewsModel.objects.all()[:half]
        ids = DemoNewsModel.objects.all()

        for id in ids:
            NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty'
            headers = {'user-agent': 'quickcheck/0.0.1'}
            response = requests.get(NEWS_URL, headers=headers)
            data = json.loads(response.text)
            result.append(data)

        return result


# GET the latest hackernews streamed

    def get(self, request, format=None):
        return Response(self.get_data_from_API(), status=status.HTTP_201_CREATED)



def newsItemView(request):
    result = []
    ids = DemoNewsModel.objects.all()[:20]
    for id in ids:
        NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        data = json.loads(response.text)
        result.append(data)

    # return result
    p = Paginator(result, 5)
    page = request.GET.get('page')
    news = p.get_page(page)
    nums = "1" * news.paginator.num_pages

    return render(request, 'news/news.html', {'news': news, 'news_list':  result, "nums": nums})