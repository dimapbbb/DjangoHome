from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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
    fields = ('title', 'content', 'picture', 'publication_sign')
    success_url = '/blog'

    def get_context_data(self, **kwargs):
        """ Получение данных контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Новая запись"
        return context


class UserPostDetailView(DetailView):
    model = UserPost


class UserPostUpdateView(UpdateView):
    model = UserPost
    fields = ('title', 'content', 'picture', 'publication_sign')
    success_url = '/blog'


class UserPostDeleteView(DeleteView):
    model = UserPost
    success_url = '/blog'
