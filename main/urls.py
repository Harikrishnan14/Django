from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('questions/', views.QuestionListView.as_view(), name="questionList"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="questionDetail"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="questionCreate"),
]
