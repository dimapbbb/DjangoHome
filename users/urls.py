from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, user_authentication, RestorePassword, UserExit

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', UserExit.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_authentication', user_authentication, name='user_authentication'),
    path('restore_password/', RestorePassword.as_view(), name='restore_password'),
    # path('verification/<str:secret_cod>/', VerificationView.as_view(), name='verification'),

]
