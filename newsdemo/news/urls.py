from django.urls import path
from .views import get_data_from_API, newsItemView

urlpatterns = [
    path('hackernews/', get_data_from_API, name='news-item'), 
    # http://127.0.0.1:8080/api/v0/items/hackernews --> GET the latest hackernews from db
    path('news/', newsItemView, name='news'),
]