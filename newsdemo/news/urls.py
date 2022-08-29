from django.urls import path
from .views import NewsIdView, NewsItemView

urlpatterns = [
    path('all/', NewsIdView.as_view(), name='index'),
    # http://127.0.0.1:8080/api/v0/items/all --> lists all news id from hackernews endpoint
    path('hackernews/', NewsItemView.as_view(), name='news-item'), 
    # http://127.0.0.1:8080/api/v0/items/hackernews --> GET the latest hackernews from db
]