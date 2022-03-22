from django.urls import path
from .views import NewsList, Whole_newsDetail



urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', Whole_newsDetail.as_view()),
]
