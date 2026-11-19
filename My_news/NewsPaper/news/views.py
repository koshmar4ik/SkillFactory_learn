from django.shortcuts import render
from django.template.defaultfilters import length

# Create your views here.
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import News
from django.urls import reverse_lazy


class Posts(ListView):
    model = Post
    ordering = '-create_time'
    template_name = 'news.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'


class Create(CreateView):
    form_class = News
    model = Post
    template_name = 'create.html'

    def form_valid(self, form):
        news = form.save(commit = False)
        context = self.get_context_data()
        if context["types"] == "Новость":
            news.category_type = "ns"
        else:
            news.category_type = "ae"
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parts = [p for p in self.request.path.split("/") if p]
        context["types"] = "Новость" if parts[-2] == 'post' else "Статья"
        return context


class Editing(UpdateView):
    form_class = News
    model = Post
    template_name = 'create.html'

class Editing(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('head')