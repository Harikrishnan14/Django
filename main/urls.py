from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('questions/', views.QuestionListView.as_view(), name="questionList"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="questionDetail"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="questionCreate"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="questionUpdate"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name="questionDelete"),
    
]
