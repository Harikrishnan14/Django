from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('questions/', views.QuestionListView.as_view(), name="questionList"),
]
