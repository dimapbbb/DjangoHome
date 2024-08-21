from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import UserPost


class UserPostListView(ListView):
    model = UserPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset

    def get_context_data(self, **kwargs):
        """ Получение контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Блог"
        return context


class UserPostCreateView(CreateView):
    model = UserPost
    fields = ('title', 'content', 'picture', 'publication_sign')
    success_url = '/blog'

    def form_valid(self, form):
        if form.is_valid():
            new_userpost = form.save()
            new_userpost.slug = slugify(new_userpost.title)
            new_userpost.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Получение данных контекста """
        context = super().get_context_data(**kwargs)
        context["title"] = "Новая запись"
        return context


class UserPostDetailView(DetailView):
    model = UserPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class UserPostUpdateView(UpdateView):
    model = UserPost
    fields = ('title', 'content', 'picture', 'publication_sign')

    def form_valid(self, form):
        if form.is_valid():
            new_userpost = form.save()
            new_userpost.slug = slugify(new_userpost.title)
            new_userpost.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view_post', args=[self.kwargs.get("pk")])


class UserPostDeleteView(DeleteView):
    model = UserPost
    success_url = '/blog'
