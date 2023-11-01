from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = something.total_likes()
        liked = False
        if something.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


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
        
class CommentDetailView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'question_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('/questions')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    template_name = 'main/question_comment.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('main:questionList')

def LikeView(request, pk):
    post = get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('main:questionDetail', args=[str(pk)]))
