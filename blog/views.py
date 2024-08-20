from django.views.generic import CreateView, ListView

from blog.models import UserPost


class UserPostListView(ListView):
    model = UserPost

    def get_context_data(self, **kwargs):
        """ Получение контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Блог"
        return context


class UserPostCreateView(CreateView):
    model = UserPost
    fields = ('title', 'content', 'picture')
    success_url = '/blog'

    def get_context_data(self, **kwargs):
        """ Получение данных контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Новая запись"
        return context
