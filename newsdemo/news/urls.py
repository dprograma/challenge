from django.urls import path
from .views import get_data_from_API, newsItemView

urlpatterns = [
    path('hackernews/', get_data_from_API, name='news-item'), 
    # http://127.0.0.1:8000/api/v0/items/hackernews --> GET the latest hackernews from db
     path('hackernews-post/', get_data_from_API, name='news-item-post'), 
    # http://127.0.0.1:8000/api/v0/items/hackernews-post --> POST custom news to local db
    path('news/', newsItemView, name='news'),
]