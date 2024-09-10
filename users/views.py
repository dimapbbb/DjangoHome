import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from config import settings
from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()

            send_mail(
                "Регистрация нового пользователя",
                f"Успешная регистрация на сайте",
                settings.EMAIL_HOST_USER,
                [user.email]
            )
        return redirect('catalog:products')

    def get_success_url(self):
        return reverse_lazy('users:login')


class RestorePassword(TemplateView):
    template_name = 'restore_password.html'

    def post(self, request, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        new_password = ""
        if user:
            for i in range(8):
                symbol = random.randint(0, 9)
                new_password += str(symbol)

            send_mail(
                "new_password",
                f'Новый пароль : {new_password}',
                settings.EMAIL_HOST_USER,
                [email]
            )

            user.password = make_password(new_password)
            user.save()
        return redirect('users:login')


class UserExit(TemplateView):
    template_name = 'logged_out.html'

    def post(self, request):
        request.session.delete()
        return redirect('catalog:Home')


def user_authentication(request):
    return render(request, 'user_authentication.html')
