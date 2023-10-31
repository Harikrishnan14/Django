from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, 'home.html')


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'content']

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False
        
class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    context_object_name = 'questions'
    success_url = "/questions"
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False