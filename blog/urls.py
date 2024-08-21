from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import UserPostListView, UserPostCreateView, UserPostDetailView, UserPostUpdateView, UserPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', UserPostListView.as_view(), name='blogview'),
    path('create/', UserPostCreateView.as_view(), name='create_post'),
    path('view/<int:pk>/', UserPostDetailView.as_view(), name='view_post'),
    path('edit/<int:pk>/', UserPostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', UserPostDeleteView.as_view(), name='delete_post')
]
