from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BaseRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        user.groups.add(premium_group)
    return redirect('/')