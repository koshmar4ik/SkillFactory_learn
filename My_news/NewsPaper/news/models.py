from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
#from django.utils.text import truncate_words
# Create your models here.


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.authorUser.username

    def update_rating(self):
        postRat = self.post_set.all().aggregate(sum=Sum('rating_post'))['sum']
        if postRat is None:
            postRat = 0
        commRat = self.authorUser.comment_set.all().aggregate(sum=Sum('rating_comments'))['sum']
        if commRat is None:
            commRat = 0
        comsRat = Comment.objects.filter(post_link__author=self).aggregate(sum=Sum('rating_comments'))['sum']
        if comsRat is None:
            comsRat = 0
        self.rating = postRat * 3 + commRat + comsRat
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True, default='Free')


class Post(models.Model):
    news = 'ns'
    article = 'ae'

    TYPES = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=2, choices=TYPES, default=news)
    create_time = models.DateTimeField(auto_now_add = True)
    link_category = models.ManyToManyField(Category, through='PostCategory')
    head = models.CharField(max_length=255)
    posts = models.TextField()
    rating_post = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.head} {self.posts[:124]} "..."'


    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()


class PostCategory(models.Model):
    post_link = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_link = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_link = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_link = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.user_link.username

    def like(self):
        self.rating_comments += 1
        self.save()

    def dislike(self):
        self.rating_comments -= 1
        self.save()