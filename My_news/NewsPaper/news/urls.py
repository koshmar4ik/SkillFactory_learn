from django.urls import path
# Импортируем созданное нами представление
from .views import Posts, NewsDetail, Create, Editing, Delete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', Posts.as_view(), name='head'),
    path('<int:pk>/', NewsDetail.as_view(), name='detail_news'),
    path('post/create/', Create.as_view(), name='create_news'),
    path('article/create/', Create.as_view(), name='create_article'),
    path('article/<int:pk>/edit/', Editing.as_view(), name='edit_article'),
    path('post/<int:pk>/edit/', Editing.as_view(), name='edit_news'),
    path('article/<int:pk>/delete/', Delete.as_view(), name='delete_article'),
    path('post/<int:pk>/delete/', Delete.as_view(), name='delete_news'),
    ]