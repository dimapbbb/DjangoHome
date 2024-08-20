from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import UserPostListView, UserPostCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', UserPostListView.as_view(), name='blogview'),
    path('create/', UserPostCreateView.as_view(), name='create-post'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
